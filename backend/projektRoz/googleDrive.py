from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
import io
import logging

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = '/app/projektRoz/service.json'

class GoogleDriveManager:
    """
    A class that provides methods for managing files and folders on Google Drive.

    Attributes:
        service_account_file (str): The path to the service account file.
        scopes (list): The list of scopes for authentication.

    Methods:
        __init__(self, service_account_file, scopes): Initializes the GoogleDriveManager instance.
        authenticate(self): Authenticates the Google Drive service account.
        get_folder_id(self, folder_name, parent_id): Retrieves the ID of a folder with the given name.
        create_folder(self, folder_name, parent_id): Creates a new folder with the given name.
        ensure_folder_exists(self, folder_path, parent_id): Ensures that a folder with the given path exists.
        upload_file(self, name, file_obj, folder_id): Uploads a file to the specified folder.
        check_if_file_exists(self, file_name, folder_id, count): Checks if a file with the given name exists in the folder.
        get_files(self, folder_id): Retrieves the list of files in the specified folder.
        get_download_url(self, file_id): Retrieves the download URL for a file with the given ID.
        download_file(self, file_id, destination): Downloads a file with the given ID to the specified destination.
        deleteFileById(self, file_id): Deletes a file with the given ID.

    """
    logger = logging.getLogger(__name__)

    def __init__(self, service_account_file=SERVICE_ACCOUNT_FILE, scopes=SCOPES):
        """
        Initializes the GoogleDriveManager instance.

        Args:
            service_account_file (str, optional): The path to the service account file. Defaults to SERVICE_ACCOUNT_FILE.
            scopes (list, optional): The list of scopes for authentication. Defaults to SCOPES.
        """
        self.service_account_file = service_account_file
        self.scopes = scopes
        self.creds = self.authenticate()
        self.service = build('drive', 'v3', credentials=self.creds)

    def authenticate(self):
        """
        Authenticates the Google Drive service account.

        Returns:
            Credentials: The authenticated credentials.
        """
        credentials = service_account.Credentials.from_service_account_file(
            self.service_account_file, scopes=self.scopes)
        return credentials

    def get_folder_id(self, folder_name, parent_id=None):
        """
        Retrieves the ID of a folder with the given name and optional parent ID.

        Args:
            folder_name (str): The name of the folder to search for.
            parent_id (str, optional): The ID of the parent folder. Defaults to None.

        Returns:
            str or None: The ID of the folder if found, None otherwise.
        """
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
        """
        Creates a new folder in Google Drive.

        Args:
            folder_name (str): The name of the folder to be created.
            parent_id (str, optional): The ID of the parent folder. Defaults to None.

        Returns:
            str: The ID of the newly created folder.
        """
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
        """
        Ensures that a folder exists in Google Drive with the given folder path.
        
        Args:
            folder_path (str): The path of the folder to be created.
            parent_id (str, optional): The ID of the parent folder where the new folder should be created. Defaults to None.
        
        Returns:
            str: The ID of the created or existing folder.
            None: If an error occurs during the process.
        """
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
        """
        Uploads a file to Google Drive.

        Args:
            name (str): The name of the file.
            file_obj (file-like object): The file object to be uploaded.
            folder_id (str): The ID of the folder where the file will be uploaded.

        Returns:
            list: A list containing the ID and name of the uploaded file.

        Raises:
            HttpError: If an error occurs during the upload process.
        """
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
        """
        Checks if a file with the given name exists in the specified folder.

        Args:
            file_name (str): The name of the file to check.
            folder_id (str): The ID of the folder to search in.
            count (int, optional): The count of files with the same name. Defaults to 0.

        Returns:
            int: The count of files with the same name in the folder.
        """
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
        """
        Retrieves a list of files within a specified folder.

        Args:
            folder_id (str): The ID of the folder to retrieve files from.

        Returns:
            list: A list of dictionaries representing the files, each containing the 'id', 'name', and 'mimeType' properties.
        """
        results = self.service.files().list(
            q=f"'{folder_id}' in parents",
            spaces='drive',
            fields='files(id, name, mimeType)'
        ).execute()

        items = results.get('files', [])
        return items


    def get_download_url(self, file_id):
        """
        Returns the download URL for a file with the given file ID.

        Parameters:
        - file_id (str): The ID of the file to get the download URL for.

        Returns:
        - str: The download URL for the file.
        """
        return f"https://drive.google.com/uc?export=download&id={file_id}"

    def download_file(self, file_id, destination):
        """
        Downloads a file from Google Drive.

        Args:
            file_id (str): The ID of the file to download.
            destination (str): The destination directory to save the downloaded file.

        Returns:
            str: The path of the downloaded file.

        Raises:
            Any exceptions that may occur during the file download process.
        """
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

    def deleteFileById(self, file_id):
        try:
            self.service.files().delete(fileId=file_id).execute()
            return True
        except Exception as e:
            raise e