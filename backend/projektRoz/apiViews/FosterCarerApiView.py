from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import FosterCarer
from projektRoz.serializer import FosterCarerSerializer

class FosterCarerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, foster_career_id = None, *args, **kwargs):
        if foster_career_id is None:
            foster_career = FosterCarer.objects.all().order_by('id')
        else:
            foster_career = FosterCarer.objects.filter(id = foster_career_id)
            
        serializer = FosterCarerSerializer(foster_career, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = FosterCarerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, foster_career_id, *args, **kwargs):
        foster_career = FosterCarer.objects.get(id = foster_career_id)
        
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
        foster_career = FosterCarer.objects.get(id = foster_career_id)
        
        if foster_career is not None:
            foster_career.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)