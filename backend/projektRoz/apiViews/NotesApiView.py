from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Notes
from projektRoz.serializer import NotesSerializer

class NotesApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, note_id = None, *args, **kwargs):
        if note_id is None:
            note = Notes.objects.all().order_by('id')
        else:
            note = Notes.objects.filter(id = note_id)
            
        serializer = NotesSerializer(note, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, note_id, *args, **kwargs):
        note = Notes.objects.get(id = note_id)
        
        if note is not None:
            serializer = NotesSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif note is None:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, note_id, *args, **kwargs):
        note = Notes.objects.get(id = note_id)
        
        if note is not None:
            note.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)