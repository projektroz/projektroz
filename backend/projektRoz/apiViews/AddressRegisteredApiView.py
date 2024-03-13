from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import AddressRegistered
from projektRoz.serializer import AddressRegisteredSerializer

class AddressRegisteredApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, address_registered_id = None, *args, **kwargs):
        if address_registered_id is None:
            address_registered = AddressRegistered.objects.all().order_by('id')
        else:
            address_registered = AddressRegistered.objects.filter(id = address_registered_id)
            
        serializer = AddressRegisteredSerializer(address_registered, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = AddressRegisteredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, address_registered_id, *args, **kwargs):
        address_registered = AddressRegistered.objects.get(id = address_registered_id)
        
        if address_registered is not None:
            serializer = AddressRegisteredSerializer(address_registered, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif address_registered is None:
            serializer = AddressRegisteredSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, address_registered_id, *args, **kwargs):
        address_registered = AddressRegistered.objects.get(id = address_registered_id)
        
        if address_registered is not None:
            address_registered.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)