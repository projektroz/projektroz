from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from projektRoz.models import Child, FosterCarer, Notes
from projektRoz.serializer import NotesSerializer


class NotesApiView(APIView):
    """API view for managing notes."""

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "note_id",
                openapi.IN_QUERY,
                description="ID of the note",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "page",
                openapi.IN_QUERY,
                description="Page number must be greater than 0 or else get method will return all data",
                type=openapi.TYPE_INTEGER,
            ),
        ],
        responses={200: NotesSerializer(many=True), 404: "Not Found"},
    )
    def get(self, request, note_id=None, *args, **kwargs):
        """Retrieve a list of notes or a specific note by ID.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to retrieve (optional).

        Returns:
        - Response: The serialized note(s) data.
        """

        page = int(request.data.get("page")) if request.data.get("page") else None

        if note_id:
            try:
                note = Notes.objects.get(id=note_id)
                child = Child.objects.get(id=note.child.id)
                fosterCarer = FosterCarer.objects.get(id=request.user.id)
            except BaseException:
                return Response(status=status.HTTP_204_NO_CONTENT)

            if child.foster_carer == fosterCarer:
                serializer = NotesSerializer(note, many=False)

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            fosterCarer = FosterCarer.objects.get(id=request.user.id)
            children = Child.objects.filter(foster_carer=fosterCarer)
            notes = Notes.objects.all()

            ret = []

            for child in children:
                for note in notes:
                    if child.id == note.child.id:
                        ret.append(note)

            if ret != []:
                if page:
                    start = 5 * (page - 1)
                    end = 5 + 5 * (page - 1)
                    serializer = NotesSerializer(ret[start:end], many=True)
                else:
                    serializer = NotesSerializer(ret, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        request_body=NotesSerializer,
        responses={201: NotesSerializer, 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        """Create a new note.

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

    @swagger_auto_schema(
        request_body=NotesSerializer,
        responses={200: NotesSerializer, 404: "Not Found", 400: "Bad Request"},
    )
    def put(self, request, note_id=None, *args, **kwargs):
        """Update an existing note.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to update.

        Returns:
        - Response: The serialized note data if successful, or the error message if validation fails.
        """
        if note_id:
            note = Notes.objects.get(id=note_id)
            child = Child.objects.get(id=note.child.id)
            fosterCarer = FosterCarer.objects.get(id=request.user.id)

            if child.foster_carer == fosterCarer:
                serializer = NotesSerializer(note, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(responses={204: "No Content", 404: "Not Found"})
    def delete(self, request, note_id, *args, **kwargs):
        """Delete a note.

        Parameters:
        - request: The request object.
        - note_id: The ID of the note to delete.

        Returns:
        - Response: No content if successful, or the error message if the note is not found.
        """
        note = Notes.objects.get(id=note_id)
        child = Child.objects.get(id=note.child.id)
        fosterCarer = FosterCarer.objects.get(id=request.user.id)

        if child.foster_carer == fosterCarer:
            note.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)
