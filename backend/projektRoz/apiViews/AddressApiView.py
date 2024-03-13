from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Address
from projektRoz.serializer import AddressSerializer

class AddressApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, address_id = None, *args, **kwargs):
        if address_id is None:
            address = Address.objects.all().order_by('id')
        else:
            address = Address.objects.filter(id = address_id)
            
        serializer = AddressSerializer(address, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, address_id, *args, **kwargs):
        address = Address.objects.get(id = address_id)
        
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
        address = Address.objects.get(id = address_id)
        
        if address is not None:
            address.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)