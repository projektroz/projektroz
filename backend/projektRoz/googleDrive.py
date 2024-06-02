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

    def ensure_folder_exists(self, folder_name, parent_id=None):
        try:
            folder_id = self.get_folder_id(folder_name, parent_id)
            if folder_id:
                print(f"Folder '{folder_name}' already exists with ID: {folder_id}")
            else:
                folder_id = self.create_folder(folder_name, parent_id)
                print(f"Folder '{folder_name}' created with ID: {folder_id}")

            return folder_id

        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def upload_file(self, name, file_obj, folder_id):
        file_metadata = {
            'name': name,
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
        except HttpError as error:
            print(f"An error occurred: {error}")
            raise

    def get_files(self, folder_id):
        results = self.service.files().list(
            q=f"'{folder_id}' in parents",
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        items = results.get('files', [])
        return items

    def get_download_url(self, file_id):
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    def download_file(self, file_id, destination):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.FileIO(destination, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while not done:
            status, done = downloader.next_chunk()
            self.logger.debug(f"Download {int(status.progress() * 100)}%.")
