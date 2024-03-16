from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Mother
from projektRoz.serializer import MotherSerializer

class MotherApiView(APIView):
    """
    API view for interacting with the Mother model.

    Methods:
    - get: Retrieves a list of all mothers or a specific mother by ID.
    - post: Creates a new mother.
    - put: Updates an existing mother by ID.
    - delete: Deletes a mother by ID.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, mother_id = None, *args, **kwargs):
        """
        Retrieves a list of all mothers or a specific mother by ID.

        Parameters:
        - request: The request object.
        - mother_id (optional): The ID of the mother to retrieve.

        Returns:
        - Response: The serialized data of the mother(s).
        """
        if mother_id is None:
            mother = Mother.objects.all().order_by('id')
        else:
            mother = Mother.objects.filter(id = mother_id)
            
        serializer = MotherSerializer(mother, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
        Creates a new mother.

        Parameters:
        - request: The request object.

        Returns:
        - Response: The serialized data of the created mother.
        """
        serializer = MotherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, mother_id, *args, **kwargs):
        """
        Updates an existing mother by ID.

        Parameters:
        - request: The request object.
        - mother_id: The ID of the mother to update.

        Returns:
        - Response: The serialized data of the updated mother.
        """
        mother = Mother.objects.get(id = mother_id)
        
        if mother is not None:
            serializer = MotherSerializer(mother, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif mother is None:
            serializer = MotherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, mother_id, *args, **kwargs):
        """
        Deletes a mother by ID.

        Parameters:
        - request: The request object.
        - mother_id: The ID of the mother to delete.

        Returns:
        - Response: A success status indicating the deletion.
        """
        mother = Mother.objects.get(id = mother_id)
        
        if mother is not None:
            mother.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)