from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from projektRoz.googleDrive import upload_photo

class FileApiView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('file')  # Pobierz przesłany plik
        name = request.data.get('name')  # Pobierz wartość przesłaną w ramce "name"
        
        if file_obj:
            try:
                # Tutaj przesyłasz plik na Google Drive wraz z nazwą
                upload_photo(name, file_obj)
                return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)