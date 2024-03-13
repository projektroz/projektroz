from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Child
from projektRoz.serializer import ChildSerializer

class ChildrenApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, child_id = None, *args, **kwargs):
        if child_id is None:
            children = Child.objects.all().order_by('id')
        else:
            children = Child.objects.filter(id = child_id)
        serializer = ChildSerializer(children, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, child_id, *args, **kwargs):
        child = Child.objects.get(id = child_id)
        
        if child is not None:
            serializer = ChildSerializer(child, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif child is None:
            serializer = ChildSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, child_id, *args, **kwargs):
        child = Child.objects.get(id = child_id)
        
        if child is not None:
            child.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)