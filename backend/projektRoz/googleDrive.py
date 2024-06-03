from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
import io
import logging

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/app/projektRoz/service.json'

class GoogleDriveManager:
    logger = logging.getLogger(__name__)

    def __init__(self, service_account_file=SERVICE_ACCOUNT_FILE, scopes=SCOPES):
        self.service_account_file = service_account_file
        self.scopes = scopes
        self.creds = self.authenticate()
        self.service = build('drive', 'v3', credentials=self.creds)

    def authenticate(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_file, scopes=self.scopes)
        return credentials

    def get_folder_id(self, folder_name, parent_id=None):
        query = f"mimeType='application/vnd.google-apps.folder' and name='{folder_name}'"
        if parent_id:
            query += f" and '{parent_id}' in parents"

        results = self.service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        items = results.get('files', [])
        if items:
            return items[0]['id']
        else:
            return None

    def create_folder(self, folder_name, parent_id=None):
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            folder_metadata['parents'] = [parent_id]

        folder = self.service.files().create(
            body=folder_metadata,
            fields='id'
        ).execute()

        return folder.get('id')

    def ensure_folder_exists(self, folder_path, parent_id=None):
        try:
            folders = folder_path.split('/')
            current_parent_id = parent_id

            for folder_name in folders:
                folder_id = self.get_folder_id(folder_name, current_parent_id)
                if folder_id:
                    print(f"Folder '{folder_name}' already exists with ID: {folder_id}")
                else:
                    folder_id = self.create_folder(folder_name, current_parent_id)
                    print(f"Folder '{folder_name}' created with ID: {folder_id}")

                current_parent_id = folder_id

            return current_parent_id

        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def upload_file(self, name, file_obj, folder_id):
        num_of_files = self.check_if_file_exists(name, folder_id)
        file_metadata = {
            'name': name + f"_{num_of_files}" if num_of_files != 0 else name,
            'parents': [folder_id]
        }

        file_io = io.BytesIO(file_obj.read())
        media_body = MediaIoBaseUpload(file_io, mimetype=file_obj.content_type, resumable=True)

        try:
            file = self.service.files().create(
                body=file_metadata,
                media_body=media_body
            ).execute()
            print(f"Uploaded file with ID: {file.get('id')}")
            return [file.get('id'), file.get('name')]
        except HttpError as error:
            print(f"An error occurred: {error}")
            raise

    def check_if_file_exists(self, file_name, folder_id, count=0):
        results = self.service.files().list(
            q=f"'{folder_id}' in parents and name='{file_name if count == 0 else file_name + f'_{count}'}'",
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        items = results.get('files', [])
        
        if len(items) > 0:
            return self.check_if_file_exists(file_name, folder_id, count + 1)

        return count


    def get_files(self, folder_id):
        results = self.service.files().list(
            q=f"'{folder_id}' in parents",
            spaces='drive',
            fields='files(id, name, mimeType)'
        ).execute()

        items = results.get('files', [])
        return items


    def get_download_url(self, file_id):
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    def download_file(self, file_id, destination):
        request = self.service.files().get_media(fileId=file_id)
        fileType = self.service.files().get(fileId=file_id).execute()['mimeType']
        fileName = self.service.files().get(fileId=file_id).execute()['name']

        extension = ''
        if fileType == 'application/vnd.google-apps.document':
            extension = 'docx'
        elif fileType == 'application/vnd.google-apps.spreadsheet':
            extension = 'xlsx'
        elif fileType == 'application/vnd.google-apps.presentation':
            extension = 'pptx'
        elif fileType == 'application/vnd.google-apps.drawing':
            extension = 'jpg'
        elif fileType == 'application/vnd.google-apps.script':
            extension = 'json'
        elif fileType == 'text/plain':
            extension = 'txt'
        else:
            extension = fileType.split('/')[-1]

        destination = f"{destination}/{fileName}.{extension}"

        fh = io.FileIO(destination, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            self.logger.debug(f"Download {int(status.progress() * 100)}%.")

        return destination
