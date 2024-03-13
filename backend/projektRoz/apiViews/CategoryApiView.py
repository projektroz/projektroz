from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Category
from projektRoz.serializer import CategorySerializer

class CategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, category_id = None, *args, **kwargs):
        if category_id is None:
            category = Category.objects.all().order_by('id')
        else:
            category = Category.objects.filter(id = category_id)
            
        serializer = CategorySerializer(category, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, category_id, *args, **kwargs):
        category = Category.objects.get(id = category_id)
        
        if category is not None:
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif category is None:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id, *args, **kwargs):
        category = Category.objects.get(id = category_id)
        
        if category is not None:
            category.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)