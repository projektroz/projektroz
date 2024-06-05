import base64
import logging
import mimetypes
import os

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from projektRoz.googleDrive import GoogleDriveManager
from projektRoz.models import AllowedCategories, Child, Documents


class FileApiView(APIView):
    """API view for handling file uploads, downloads, and deletions.

    This view provides endpoints for uploading files, retrieving files, and deleting files.
    It supports multipart/form-data requests for file uploads.

    Endpoints:
    - POST: Upload a file.
    - GET: Retrieve a file or a list of files.
    - DELETE: Delete a file.

    The view uses Google Drive as the storage backend for file operations.

    Attributes:
    - parser_classes (tuple): The parser classes used for parsing the request data.
    - logger (Logger): The logger instance for logging messages.

    Methods:
    - post: Handle file upload requests.
    - get: Handle file retrieval requests.
    - delete: Handle file deletion requests.
    - get_files_recursively: Recursively retrieve files from a folder in Google Drive.
    - sendFile: Upload a file to Google Drive.
    - handle_photo_upload: Handle file upload requests specifically for profile photos.
    """

    parser_classes = (MultiPartParser, FormParser)
    logger = logging.getLogger(__name__)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "file",
                openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                description="File to upload",
            ),
            openapi.Parameter(
                "name",
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="Name of the file",
            ),
            openapi.Parameter(
                "child_id",
                openapi.IN_FORM,
                type=openapi.TYPE_INTEGER,
                description="ID of the child, not mandatory if file_type is 'schematy'",
            ),
            openapi.Parameter(
                "file_type",
                openapi.IN_FORM,
                type=openapi.TYPE_STRING,
                description="Type of the file",
                enum=[category.value for category in AllowedCategories],
            ),
        ],
        responses={
            201: openapi.Response("File uploaded successfully"),
            400: openapi.Response("No file provided"),
            500: openapi.Response("Internal server error"),
        },
    )
    def post(self, request, *args, **kwargs):
        """Handle the HTTP POST request for uploading a file.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A Response object with the result of the file upload.

        Raises:
            Child.DoesNotExist: If the child with the specified ID does not exist.
        """
        file_obj = request.FILES.get("file")
        name = request.data.get("name")
        child_id = request.data.get("child_id")
        file_type = request.data.get("file_type")
        googleDriveManager = GoogleDriveManager()

        if file_type not in [category.value for category in AllowedCategories]:
            return Response(
                {"error": f"{AllowedCategories.choices}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.logger.info(f"Uploading file for child with ID: {child_id}")

        try:
            if file_type == AllowedCategories.SCHEMATY.value:
                drive_path = f"projektRoz/Schematy"
            else:
                try:
                    child = Child.objects.get(id=child_id)
                except Child.DoesNotExist:
                    return Response(
                        {"error": "Child not found"}, status=status.HTTP_404_NOT_FOUND
                    )

                if file_obj and file_type == AllowedCategories.ZDJECIE.value:
                    if file_obj.name.split(".")[-1].lower() not in [
                        "jpg",
                        "jpeg",
                        "png",
                        "gif",
                        "bmp",
                        "webp",
                    ]:
                        return Response(
                            {"error": "Invalid file format"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                    drive_path = f"projektRoz/{child.surname}_{child.name}_{child_id}"
                    name = "profile_photo"
                    return self.handle_photo_upload(
                        name, file_obj, drive_path, child, file_type, googleDriveManager
                    )
                else:
                    drive_path = f"projektRoz/{child.surname}_{child.name}_{child_id}/{file_type}"

        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return Response(
                {"error": "An error occurred while processing the request"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if file_obj:
            fileData = self.sendFile(name, file_obj, drive_path, googleDriveManager)
            return Response(
                {
                    "message": "File uploaded successfully",
                    "file_id": f"{fileData[0]}",
                    "file_path": f"{drive_path}/{fileData[1]}",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                "List of files",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "id": openapi.Schema(type=openapi.TYPE_STRING),
                            "name": openapi.Schema(type=openapi.TYPE_STRING),
                            "download_url": openapi.Schema(type=openapi.TYPE_STRING),
                        },
                    ),
                ),
            ),
            500: openapi.Response("Internal server error"),
        }
    )
    def get(self, request, *args, **kwargs):
        """Retrieves a file from Google Drive or a list of files in a folder.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the file data or a list of files.

        Raises:
            Exception: If there is an error while retrieving the file(s) from Google Drive.
        """
        file_id = kwargs.get("id")
        if file_id:
            try:
                googleDriveManager = GoogleDriveManager()

                destination = f"projektRoz/resources/"

                local_file_path = googleDriveManager.download_file(file_id, destination)

                with open(local_file_path, "rb") as file:
                    file_data = file.read()
                    mime_type, _ = mimetypes.guess_type(local_file_path)
                    if not mime_type:
                        mime_type = "application/octet-stream"

                    encoded_file = base64.b64encode(file_data).decode("utf-8")

                os.remove(local_file_path)

                return Response(
                    {
                        "file_name": os.path.basename(local_file_path),
                        "file_data": encoded_file,
                        "mime_type": mime_type,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            try:
                googleDriveManager = GoogleDriveManager()

                folder_id = googleDriveManager.get_folder_id("projektRoz")
                files = self.get_files_recursively(folder_id)
                return Response(files, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def delete(self, request, *args, **kwargs):
        """Deletes a file from the server and Google Drive.

        Args:
            request: The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            A Response object with a success message if the file is deleted successfully,
            or an error message if an exception occurs.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        file_id = kwargs.get("id")
        try:
            googleDriveManager = GoogleDriveManager()
            googleDriveManager.deleteFileById(file_id)
            Documents.objects.get(document_google_id=file_id).delete()
            return Response(
                {"message": "File deleted successfully"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_files_recursively(self, folder_id):
        """Recursively retrieves all files and subfolders within a given
        folder.

        Args:
            folder_id (str): The ID of the folder to retrieve files from.

        Returns:
            list: A list of dictionaries representing the files and subfolders within the given folder.
                  Each dictionary contains information such as file name, ID, MIME type, and download URL (for files).
        """
        googleDriveManager = GoogleDriveManager()
        files = googleDriveManager.get_files(folder_id)

        for file in files:
            if file["mimeType"] == "application/vnd.google-apps.folder":
                subfolder_id = file["id"]
                subfolder_files = self.get_files_recursively(subfolder_id)
                file["subfolder_files"] = subfolder_files
            else:
                file["download_url"] = googleDriveManager.get_download_url(file["id"])

        return files

    def sendFile(self, name, file_obj, drive_path, googleDriveManager):
        """Sends a file to Google Drive.

        Args:
            name (str): The name of the file.
            file_obj (file-like object): The file object to be uploaded.
            drive_path (str): The path to the Google Drive folder where the file should be uploaded.
            googleDriveManager (GoogleDriveManager): An instance of the GoogleDriveManager class.

        Returns:
            str: The ID of the uploaded file on Google Drive.

        Raises:
            Exception: If an error occurs during the file upload.
        """
        try:
            folder_id = googleDriveManager.ensure_folder_exists(drive_path)
            return googleDriveManager.upload_file(name, file_obj, folder_id)
        except Exception as e:
            raise e

    def handle_photo_upload(
        self, name, file_obj, drive_path, child, file_type, googleDriveManager
    ):
        """Handles the upload of a photo file.

        Args:
            name (str): The name of the photo file.
            file_obj (file): The file object representing the photo.
            drive_path (str): The path to the Google Drive folder where the photo will be uploaded.
            child (Child): The Child object associated with the photo.
            file_type (str): The category of the photo file.
            googleDriveManager (GoogleDriveManager): An instance of the GoogleDriveManager class.

        Returns:
            Response: A response object containing the result of the file upload.

        Raises:
            Exception: If an error occurs while uploading the photo.
        """
        try:
            photoFromDb = Documents.objects.get(document_path=drive_path + "/" + name)
            googleDriveManager.deleteFileById(photoFromDb.document_google_id)

            fileData = self.sendFile(name, file_obj, drive_path, googleDriveManager)
            photoFromDb.document_google_id = fileData[0]
            photoFromDb.document_path = drive_path + "/" + fileData[1]
            photoFromDb.save()

            return Response(
                {
                    "message": "File uploaded successfully",
                    "file_id": f"{fileData[0]}",
                    "file_path": f"{drive_path}/{fileData[1]}",
                },
                status=status.HTTP_201_CREATED,
            )

        except Documents.DoesNotExist:
            fileData = self.sendFile(name, file_obj, drive_path, googleDriveManager)
            Documents.objects.create(
                child=child,
                category=file_type,
                document_path=drive_path + "/" + fileData[1],
                document_google_id=fileData[0],
            )

            return Response(
                {
                    "message": "File uploaded successfully",
                    "file_id": f"{fileData[0]}",
                    "file_path": f"{drive_path}/{fileData[1]}",
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            self.logger.error(f"An error occurred while uploading the photo: {e}")
            return Response(
                {"error": "An error occurred while uploading the photo"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
