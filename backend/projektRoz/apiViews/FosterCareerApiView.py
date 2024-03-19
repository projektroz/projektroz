from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import FosterCareer
from projektRoz.serializer import FosterCareerSerializer

class FosterCareerApiView(APIView):
    """
    API view for interacting with fosterCareer objects.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, foster_career_id=None, *args, **kwargs):
        """
        Retrieve a list of fosterCareer objects or a specific fosterCareer object by ID.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: Optional. The ID of the fosterCareer object to retrieve.

        Returns:
        - If foster_career_id is None, returns a list of all fosterCareer objects.
        - If foster_career_id is provided, returns the specified fosterCareer object.
        """
        if foster_career_id is None:
            foster_career = FosterCareer.objects.all().order_by('id')
        else:
            foster_career = FosterCareer.objects.filter(id=foster_career_id)
            
        serializer = FosterCareerSerializer(foster_career, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
        Create a new fosterCareer object.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - If the data is valid, returns the serialized fosterCareer object with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        serializer = FosterCareerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, foster_career_id, *args, **kwargs):
        """
        Update an existing fosterCareer object.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: The ID of the fosterCareer object to update.

        Returns:
        - If the fosterCareer object exists, updates and returns the serialized fosterCareer object with status 200.
        - If the fosterCareer object does not exist, creates a new fosterCareer object and returns it with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        foster_career = FosterCareer.objects.get(id=foster_career_id)
        
        if foster_career is not None:
            serializer = FosterCareerSerializer(foster_career, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif foster_career is None:
            serializer = FosterCareerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, foster_career_id, *args, **kwargs):
        """
        Delete an existing fosterCareer object.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: The ID of the fosterCareer object to delete.

        Returns:
        - If the fosterCareer object exists, deletes it and returns status 204.
        - If the fosterCareer object does not exist, returns status 404.
        """
        foster_career = FosterCareer.objects.get(id=foster_career_id)
        
        if foster_career is not None:
            foster_career.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)