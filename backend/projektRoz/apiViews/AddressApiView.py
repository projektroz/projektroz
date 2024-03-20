from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Address, Child, FosterCareer
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
        if address_id:
            address = Address.objects.get(id=address_id)
            children = Child.objects.filter(address = address)
            fosterCareer = FosterCareer.objects.get(id = request.user.id)
            
            for child in children:
                if child.foster_career == fosterCareer:
                    serializer = AddressSerializer(address, many=False)
                    
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
        else:
            fosterCareer = FosterCareer.objects.get(id = request.user.id)
            children = Child.objects.filter(foster_career = fosterCareer)
            addresses = Address.objects.all()
            ret = []
            
            for child in children:
                for address in addresses:
                    if child.address == address:
                        ret.append(address)     
            
            serializer = AddressSerializer(ret, many=True)
                    
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
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
    
    def put(self, request, address_id = None, *args, **kwargs):
        """
        Update an existing address.

        Parameters:
        - request (Request): The HTTP request object.
        - address_id (int): The ID of the address to update.

        Returns:
        - Response: The serialized address in the response body if successful, or the error message if validation fails.
        """
        if address_id:
            address = Address.objects.get(id=address_id)
            children = Child.objects.filter(address = address)
            fosterCareer = FosterCareer.objects.get(id = request.user.id)

            for child in children:
                if child.foster_career == fosterCareer:
                    serializer = AddressSerializer(address, data = request.data)
                    if serializer.is_valid():
                        serializer.save()
                    
                        return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
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
        children = Child.objects.filter(address = address)
        fosterCareer = FosterCareer.objects.get(id = request.user.id)

        for child in children:
            if child.foster_career == fosterCareer:
                address.delete()
                    
                return Response(status=status.HTTP_204_NO_CONTENT)
        
       
        return Response(status=status.HTTP_404_NOT_FOUND)