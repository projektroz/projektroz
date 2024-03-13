from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Father
from projektRoz.serializer import FatherSerializer

class FatherApiView(APIView):
        permission_classes = [permissions.IsAuthenticated]
        
        def get(self, request, father_id = None, *args, **kwargs):
            if father_id is None:
                father = Father.objects.all().order_by('id')
            else:
                father = Father.objects.filter(id = father_id)
                
            serializer = FatherSerializer(father, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def post(self, request, *args, **kwargs):
            serializer = FatherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, father_id, *args, **kwargs):
            father = Father.objects.get(id = father_id)
            
            if father is not None:
                serializer = FatherSerializer(father, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_200_OK)
            
            elif father is None:
                serializer = FatherSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, father_id, *args, **kwargs):
            father = Father.objects.get(id = father_id)
            
            if father is not None:
                father.delete()
                
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)