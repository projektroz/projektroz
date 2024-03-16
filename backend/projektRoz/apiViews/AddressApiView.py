from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Address
from projektRoz.serializer import AddressSerializer

class AddressApiView(APIView):
    """
    API view for managing addresses.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, address_id=None, *args, **kwargs):
        """
        Retrieve a list of addresses or a specific address by ID.

        Parameters:
        - address_id (int): Optional. The ID of the address to retrieve.

        Returns:
        - Response: The serialized address(es) in the response body.
        """
        if address_id is None:
            address = Address.objects.all().order_by('id')
        else:
            address = Address.objects.filter(id=address_id)
            
        serializer = AddressSerializer(address, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """
        Create a new address.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - Response: The serialized address in the response body if successful, or the error message if validation fails.
        """
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, address_id, *args, **kwargs):
        """
        Update an existing address.

        Parameters:
        - request (Request): The HTTP request object.
        - address_id (int): The ID of the address to update.

        Returns:
        - Response: The serialized address in the response body if successful, or the error message if validation fails.
        """
        address = Address.objects.get(id=address_id)
        
        if address is not None:
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif address is None:
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, address_id, *args, **kwargs):
        """
        Delete an existing address.

        Parameters:
        - request (Request): The HTTP request object.
        - address_id (int): The ID of the address to delete.

        Returns:
        - Response: No content if successful, or the error message if the address is not found.
        """
        address = Address.objects.get(id=address_id)
        
        if address is not None:
            address.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)