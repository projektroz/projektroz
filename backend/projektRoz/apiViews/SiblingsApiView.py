from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Siblings
from projektRoz.serializer import SiblingsSerializer

class SiblingsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, siblings_id = None, *args, **kwargs):
        if siblings_id is None:
            siblings = Siblings.objects.all().order_by('id')
        else:
            siblings = Siblings.objects.filter(id = siblings_id)
            
        serializer = SiblingsSerializer(siblings, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = SiblingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, siblings_id, *args, **kwargs):
        siblings = Siblings.objects.get(id = siblings_id)
        
        if siblings is not None:
            serializer = SiblingsSerializer(siblings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif siblings is None:
            serializer = SiblingsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, siblings_id, *args, **kwargs):
        siblings = Siblings.objects.get(id = siblings_id)
        
        if siblings is not None:
            siblings.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)