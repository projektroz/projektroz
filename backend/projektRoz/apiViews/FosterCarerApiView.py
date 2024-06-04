from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import FosterCarer
from projektRoz.serializer import FosterCarerSerializer

class FosterCarerApiView(APIView):
    """
    API view for interacting with fosterCarer objects.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('foster_carer_id', openapi.IN_QUERY, description="ID of the foster carer", type=openapi.TYPE_INTEGER)
        ],
        responses={200: FosterCarerSerializer(many=False), 404: 'Not Found'}
    )
    def get(self, request, foster_carer_id = None, *args, **kwargs):
        """
        Retrieve a list of fosterCarer objects or a specific fosterCarer object by ID.

        Parameters:
        - request: The HTTP request object.
        - foster_carer_id: Optional. The ID of the fosterCarer object to retrieve.

        Returns:
        - If foster_carer_id is None, returns a list of all fosterCarer objects.
        - If foster_carer_id is provided, returns the specified fosterCarer object.
        """
        foster_carer = FosterCarer.objects.get(id = request.user.id)
        if foster_carer.id == foster_carer_id:
            serializer = FosterCarerSerializer(foster_carer, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif foster_carer_id is None:
            serializer = FosterCarerSerializer(foster_carer, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        request_body=FosterCarerSerializer,
        responses={201: FosterCarerSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new fosterCarer object.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - If the data is valid, returns the serialized fosterCarer object with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        serializer = FosterCarerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=FosterCarerSerializer,
        responses={200: FosterCarerSerializer, 404: 'Not Found', 400: 'Bad Request'}
    )
    def put(self, request, foster_carer_id = None, *args, **kwargs):
        """
        Update an existing fosterCarer object.

        Parameters:
        - request: The HTTP request object.
        - foster_carer_id: The ID of the fosterCarer object to update.

        Returns:
        - If the fosterCarer object exists, updates and returns the serialized fosterCarer object with status 200.
        - If the fosterCarer object does not exist, creates a new fosterCarer object and returns it with status 201.
        - If the data is invalid, returns the serializer errors with status 400.
        """
        if foster_carer_id:
            foster_carer = FosterCarer.objects.get(id=foster_carer_id)
            if foster_carer.id == request.user.id:
                serializer = FosterCarerSerializer(foster_carer, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                
                    return Response(serializer.data, status=status.HTTP_200_OK)
        

        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, foster_carer_id, *args, **kwargs):
        """
        Delete an existing fosterCarer object.

        Parameters:
        - request: The HTTP request object.
        - foster_carer_id: The ID of the fosterCarer object to delete.

        Returns:
        - If the fosterCarer object exists, deletes it and returns status 204.
        - If the fosterCarer object does not exist, returns status 404.
        """
        foster_carer = FosterCarer.objects.get(id=foster_carer_id)
        
        if foster_carer == request.user.id:
            foster_carer.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)