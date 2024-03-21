from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Notes, Child, FosterCarer
from projektRoz.serializer import NotesSerializer

class NotesApiView(APIView):
    """
    API view for managing notes.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, note_id=None, *args, **kwargs):
        """
        Retrieve a list of notes or a specific note by ID.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to retrieve (optional).

        Returns:
        - Response: The serialized note(s) data.
        """
        if note_id:
            note = Notes.objects.get(id=note_id)
            child = Child.objects.get(note = note)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            
            if child.foster_carer == fosterCarer:
                serializer = NotesSerializer(note, many = False)

                return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            children = Child.objects.filter(foster_carer = fosterCarer)
            notes = Notes.objects.all()
            ret = []

            for child in children:
                for note in notes:
                    if child.note == note:
                        ret.append(note)

            if ret != []:
                serializer = NotesSerializer(ret, many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
                

    def post(self, request, *args, **kwargs):
        """
        Create a new note.

        Parameters:
        - request: The request object.

        Returns:
        - Response: The serialized note data if successful, or the error message if validation fails.
        """
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, note_id = None, *args, **kwargs):
        """
        Update an existing note.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to update.

        Returns:
        - Response: The serialized note data if successful, or the error message if validation fails.
        """
        if note_id:
            note = Notes.objects.get(id=note_id)
            child = Child.objects.get(note = note)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            
            if child.foster_carer == fosterCarer:
                serializer = NotesSerializer(note, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            serializer = NotesSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, note_id, *args, **kwargs):
        """
        Delete a note.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to delete.

        Returns:
        - Response: No content if successful, or the error message if the note is not found.
        """
        note = Notes.objects.get(id=note_id)
        child = Child.objects.get(note = note)
        fosterCarer = FosterCarer.objects.get(id = request.user.id)
        
        if child.foster_carer == fosterCarer:
            note.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)