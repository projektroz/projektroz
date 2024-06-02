from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from projektRoz.googleDrive import GoogleDriveManager
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import Child
import logging
import os
import base64
import mimetypes

class FileApiView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    logger = logging.getLogger(__name__)
    allowed_file_types = ['szkola', 'sad', 'zdjecie', 'zdrowie', 'inne']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description="File to upload"),
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, description="Name of the file")
        ],
        responses={
            201: openapi.Response("File uploaded successfully"),
            400: openapi.Response("No file provided"),
            500: openapi.Response("Internal server error")
        }
    )
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')
        name = request.data.get('name')
        child_id = request.data.get('child_id')
        file_type = request.data.get('file_type')
        if file_type not in self.allowed_file_types:
            return Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

        self.logger.info(f"Uploading file for child with ID: {child_id}")

        try:
            child = Child.objects.get(id=child_id)
        except Child.DoesNotExist:
            return Response({'error': 'Child not found'}, status=status.HTTP_404_NOT_FOUND)

        drive_path = f'projektRoz/{child.surname}_{child.name}_{child_id}/{file_type}'

        if file_obj:
            try:
                googleDriveManager = GoogleDriveManager()
                folder_id = googleDriveManager.ensure_folder_exists(drive_path)
                googleDriveManager.upload_file(name, file_obj, folder_id)
                return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        responses={
            200: openapi.Response("List of files", schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_STRING),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'download_url': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            )),
            500: openapi.Response("Internal server error")
        }
    )

    def get(self, request, *args, **kwargs):
        file_id = kwargs.get('id')
        if file_id:
            try:
                googleDriveManager = GoogleDriveManager()

                destination = f'projektRoz/resources/'

                local_file_path = googleDriveManager.download_file(file_id, destination)
                
                with open(local_file_path, 'rb') as file:
                    file_data = file.read()
                    mime_type, _ = mimetypes.guess_type(local_file_path)
                    if not mime_type:
                        mime_type = 'application/octet-stream'

                    encoded_file = base64.b64encode(file_data).decode('utf-8')

                os.remove(local_file_path)

                return Response({
                    'file_name': os.path.basename(local_file_path),
                    'file_data': encoded_file,
                    'mime_type': mime_type
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            try:
                googleDriveManager = GoogleDriveManager()
                
                folder_id = googleDriveManager.get_folder_id('projektRoz')
                files = self.get_files_recursively(folder_id)
                return Response(files, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_files_recursively(self, folder_id):
        googleDriveManager = GoogleDriveManager()
        files = googleDriveManager.get_files(folder_id)

        for file in files:
            if file['mimeType'] == 'application/vnd.google-apps.folder':
                subfolder_id = file['id']
                subfolder_files = self.get_files_recursively(subfolder_id)
                file['subfolder_files'] = subfolder_files
            else:
                file['download_url'] = googleDriveManager.get_download_url(file['id'])

        return files