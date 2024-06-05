from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import Address, Child, FosterCarer
from projektRoz.serializer import AddressSerializer

class AddressApiView(APIView):
    """
    API view for managing addresses.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('type', openapi.IN_QUERY, description="Type of address ('R' for registered, 'U' for unregistered)", type=openapi.TYPE_STRING),
        openapi.Parameter('address_id', openapi.IN_QUERY, description="ID of the address", type=openapi.TYPE_INTEGER)
        ],
        responses={
            200: AddressSerializer(many=True),
            404: 'Not Found'
        }
    )
    def get(self, request, type=None, address_id=None, *args, **kwargs):
        """
        Retrieve a list of addresses or a specific address by ID.

        Parameters:
        - type (str): Optional. Specifies the type of address to retrieve ('R' for registered, 'U' for unregistered).
        - address_id (int): Optional. The ID of the address to retrieve.

        Returns:
        - Response: The serialized address(es) in the response body if successful, or a 404 error if the address is not found.
        """
        if address_id:
            address = Address.objects.get(id=address_id)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            is_registered = True if type == 'R' else False
            
            if address.is_registered == is_registered:
                children = Child.objects.filter(address=address, foster_carer=fosterCarer) | Child.objects.filter(address_registered=address, foster_carer=fosterCarer)
                if children.exists():
                    serializer = AddressSerializer(address, many=False)
                
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
        else:
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            children = Child.objects.filter(foster_carer = fosterCarer)

            is_registered = True if type == 'R' else False

            addresses = Address.objects.filter(is_registered=is_registered)
            ret = []
            
            for child in children:
                for address in addresses:
                    if child.address == address or child.address_registered == address:
                        ret.append(address)

            if ret != []:
                serializer = AddressSerializer(ret, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        request_body=AddressSerializer,
        responses={
            201: AddressSerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new address.

        Parameters:
        - request (Request): The HTTP request object.

        Returns:
        - Response: The serialized address in the response body if successful, or a 400 error if validation fails.
        """
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=AddressSerializer,
        responses={
            200: AddressSerializer,
            404: 'Not Found'
        }
    )
    def put(self, request, type=None, address_id = None, *args, **kwargs):
        """
        Update an existing address.

        Parameters:
        - request (Request): The HTTP request object.
        - type (str): Optional. Specifies the type of address to update ('R' for registered, 'U' for unregistered).
        - address_id (int): The ID of the address to update.

        Returns:
        - Response: The serialized address in the response body if successful, or a 404 error if the address is not found.
        """
        if address_id:
            address = Address.objects.get(id=address_id)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            is_registered = True if type == 'R' else False
            
            if address.is_registered == is_registered:
                children = Child.objects.filter(address=address, foster_carer=fosterCarer) | Child.objects.filter(address_registered=address, foster_carer=fosterCarer)
                if children.exists():
                    serializer = AddressSerializer(address, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    
        else:
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request, type, address_id, *args, **kwargs):
        """
        Delete an existing address.

        Parameters:
        - request (Request): The HTTP request object.
        - address_id (int): The ID of the address to delete.

        Returns:
        - Response: No content if successful, or a 404 error if the address is not found.
        """
        address = Address.objects.get(id=address_id)
        foster_carer = FosterCarer.objects.get(id = request.user.id)
        is_registered = True if type == 'R' else False

        if address.is_registered == is_registered:
            if address.is_registered:
                children = Child.objects.filter(foster_carer=foster_carer, address_registered = address)
            else:
                children = Child.objects.filter(foster_carer=foster_carer, address = address)
            
            if children.exists():
                address.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
       
        return Response(status=status.HTTP_404_NOT_FOUND)