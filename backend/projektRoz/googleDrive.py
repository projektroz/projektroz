from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseUpload
import io

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = '/app/projektRoz/service.json'
PARENT_FOLDER_ID = '1G9O1xCcsNEzxEsBKM0s9mbeV4PxRk2i6'

def authenticate():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return credentials

def upload_photo(name, file_obj):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': name,
        'parents': [PARENT_FOLDER_ID]
    }

    file_io = io.BytesIO(file_obj.read())

    media_body = MediaIoBaseUpload(file_io, mimetype=file_obj.content_type, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media_body
    ).execute()