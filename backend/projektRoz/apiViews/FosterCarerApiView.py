from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import FosterCarer
from projektRoz.serializer import FosterCarerSerializer

class FosterCarerApiView(APIView):
    """
    API view for interacting with FosterCarer objects.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, foster_career_id=None, *args, **kwargs):
        """
        Retrieve a list of FosterCarer objects or a specific FosterCarer object by ID.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: Optional. The ID of the FosterCarer object to retrieve.

        Returns:
        - If foster_career_id is None, returns a list of all FosterCarer objects.
        - If foster_career_id is provided, returns the specified FosterCarer object.
        """
        if foster_career_id is None:
            foster_career = FosterCarer.objects.all().order_by('id')
        else:
            foster_career = FosterCarer.objects.filter(id=foster_career_id)
            
        serializer = FosterCarerSerializer(foster_career, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
        Create a new FosterCarer object.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - If the data is valid, returns the serialized FosterCarer object with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        serializer = FosterCarerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, foster_career_id, *args, **kwargs):
        """
        Update an existing FosterCarer object.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: The ID of the FosterCarer object to update.

        Returns:
        - If the FosterCarer object exists, updates and returns the serialized FosterCarer object with status 200.
        - If the FosterCarer object does not exist, creates a new FosterCarer object and returns it with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        foster_career = FosterCarer.objects.get(id=foster_career_id)
        
        if foster_career is not None:
            serializer = FosterCarerSerializer(foster_career, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif foster_career is None:
            serializer = FosterCarerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, foster_career_id, *args, **kwargs):
        """
        Delete an existing FosterCarer object.

        Parameters:
        - request: The HTTP request object.
        - foster_career_id: The ID of the FosterCarer object to delete.

        Returns:
        - If the FosterCarer object exists, deletes it and returns status 204.
        - If the FosterCarer object does not exist, returns status 404.
        """
        foster_career = FosterCarer.objects.get(id=foster_career_id)
        
        if foster_career is not None:
            foster_career.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)