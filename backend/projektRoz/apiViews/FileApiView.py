from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from projektRoz.googleDrive import GoogleDriveManager
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import logging

class FileApiView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    logger = logging.getLogger(__name__)

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

        if file_obj:
            try:
                googleDriveManager = GoogleDriveManager()
                folder_id = googleDriveManager.ensure_folder_exists('projektRoz')
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
        try:
            googleDriveManager = GoogleDriveManager()
            folder_id = googleDriveManager.get_folder_id('projektRoz')
            files = googleDriveManager.get_files(folder_id)
            for file in files:
                file['download_url'] = googleDriveManager.get_download_url(file['id'])
            return Response(files, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
