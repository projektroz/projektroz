from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import Parent, Child, FosterCarer
from projektRoz.serializer import ParentSerializer

class ParentApiView(APIView):
    """
    API view for interacting with the Parent model.

    Methods:
    - get: Retrieves a list of all parents or a specific parent by ID.
    - post: Creates a new parent.
    - put: Updates an existing parent by ID.
    - delete: Deletes a parent by ID.
    """

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('role', openapi.IN_QUERY, description="Role of the parent ('M' for mother, 'F' for father)", type=openapi.TYPE_STRING),
            openapi.Parameter('parent_id', openapi.IN_QUERY, description="ID of the parent", type=openapi.TYPE_INTEGER)
        ],
        responses={200: ParentSerializer(many=True), 404: 'Not Found'}
    )
    def get(self, request, role=None, parent_id=None, *args, **kwargs):
        """
        Retrieves a list of all parents or a specific parent by ID.

        Parameters:
        - request: The request object.
        - role (optional): The role of the parent to retrieve ('M' for mother, 'F' for father).
        - parent_id (optional): The ID of the parent to retrieve.

        Returns:
        - Response: The serialized data of the parent(s).
        """
        if parent_id:
            parent = Parent.objects.get(id=parent_id)
            foster_carer = FosterCarer.objects.get(id=request.user.id)

            if parent.role == role:
                children = Child.objects.filter(mother=parent, foster_carer=foster_carer) | Child.objects.filter(father=parent, foster_carer=foster_carer)
                if children.exists():
                    serializer = ParentSerializer(parent)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                
        else:
            foster_carer = FosterCarer.objects.get(id=request.user.id)
            children = Child.objects.filter(foster_carer=foster_carer)
            parents = Parent.objects.filter(role=role)
            ret = []

            for child in children:
                for parent in parents:
                    if child.mother.id == parent.id or child.father.id == parent.id:
                        ret.append(parent)


            if ret != []:
                serializer = ParentSerializer(ret, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        request_body=ParentSerializer,
        responses={201: ParentSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        """
        Creates a new parent.

        Parameters:
        - request: The request object.

        Returns:
        - Response: The serialized data of the created parent.
        """
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            role = request.data.get('role')
            if role in ['M', 'F']:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid role. role must be 'M' for mother or 'F' for father."},
                                status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=ParentSerializer,
        responses={200: ParentSerializer, 404: 'Not Found', 400: 'Bad Request'}
    )
    def put(self, request, role=None, parent_id=None, *args, **kwargs):
        """
        Updates an existing parent by ID.

        Parameters:
        - request: The request object.
        - role (optional): The role of the parent to update ('M' for mother, 'F' for father).
        - parent_id: The ID of the parent to update.

        Returns:
        - Response: The serialized data of the updated parent.
        """
        if parent_id:
            parent = Parent.objects.get(id=parent_id)
            foster_carer = FosterCarer.objects.get(id=request.user.id)

            if parent.role == role:
                children = Child.objects.filter(mother=parent, foster_carer=foster_carer) | Child.objects.filter(father=parent, foster_carer=foster_carer)
                if children.exists():
                    serializer = ParentSerializer(parent, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    
        else:
            serializer = ParentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, role, parent_id, *args, **kwargs):
        """
        Deletes a parent by ID.

        Parameters:
        - request: The request object.
        - role: The role of the parent to delete ('M' for mother, 'F' for father).
        - parent_id: The ID of the parent to delete.

        Returns:
        - Response: A success status indicating the deletion.
        """
        parent = Parent.objects.get(id=parent_id)
        foster_carer = FosterCarer.objects.get(id=request.user.id)

        if parent.role == role:
            if parent.role == 'M':
                children = Child.objects.filter(foster_carer=foster_carer, mother=parent)
            else:
                children = Child.objects.filter(foster_carer=foster_carer, father=parent)

            if children.exists():
                parent.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
