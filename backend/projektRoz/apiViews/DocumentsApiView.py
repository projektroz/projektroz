from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Documents
from projektRoz.serializer import DocumentsSerializer

class DocumentsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, document_id = None, *args, **kwargs):
        if document_id is None:
            document = Documents.objects.all().order_by('id')
        else:
            document = Documents.objects.filter(id = document_id)
            
        serializer = DocumentsSerializer(document, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, document_id, *args, **kwargs):
        document = Documents.objects.get(id = document_id)
        
        if document is not None:
            serializer = DocumentsSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif document is None:
            serializer = DocumentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, document_id, *args, **kwargs):
        document = Documents.objects.get(id = document_id)
        
        if document is not None:
            document.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)