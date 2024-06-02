from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import Category
from projektRoz.serializer import CategorySerializer

class CategoryApiView(APIView):
    """
    API view for managing categories.
    """

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('category_id', openapi.IN_QUERY, description="ID of the category", type=openapi.TYPE_INTEGER)
        ],
        responses={200: CategorySerializer(many=True), 404: 'Not Found'}
    )
    def get(self, request, category_id = None, *args, **kwargs):
        """
        Retrieve a list of categories or a specific category by ID.
        
        Parameters:
        - request: The request object.
        - category_id: The ID of the category to retrieve (optional).
        
        Returns:
        - Response: The serialized category data or an error response.
        """
        if category_id is None:
            category = Category.objects.all().order_by('id')
        else:
            category = Category.objects.filter(id = category_id)
            
        serializer = CategorySerializer(category, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=CategorySerializer,
        responses={201: CategorySerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new category.
        
        Parameters:
        - request: The request object.
        
        Returns:
        - Response: The serialized category data or an error response.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=CategorySerializer,
        responses={200: CategorySerializer, 404: 'Not Found', 400: 'Bad Request'}
    )
    def put(self, request, category_id, *args, **kwargs):
        """
        Update an existing category or create a new category if it doesn't exist.
        
        Parameters:
        - request: The request object.
        - category_id: The ID of the category to update.
        
        Returns:
        - Response: The serialized category data or an error response.
        """
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
    
    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, category_id, *args, **kwargs):
        """
        Delete a category by ID.
        
        Parameters:
        - request: The request object.
        - category_id: The ID of the category to delete.
        
        Returns:
        - Response: A success or error response.
        """
        category = Category.objects.get(id = category_id)
        
        if category is not None:
            category.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)