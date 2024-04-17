from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

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

    def get(self, request, gender=None, parent_id=None, *args, **kwargs):
        """
        Retrieves a list of all parents or a specific parent by ID.

        Parameters:
        - request: The request object.
        - gender (optional): The gender of the parent to retrieve ('M' for mother, 'F' for father).
        - parent_id (optional): The ID of the parent to retrieve.

        Returns:
        - Response: The serialized data of the parent(s).
        """
        if parent_id:
            parent = Parent.objects.get(id=parent_id)
            foster_carer = FosterCarer.objects.get(id=request.user.id)

            if parent.gender == gender:
                children = Child.objects.filter(mother=parent, foster_carer=foster_carer) | Child.objects.filter(father=parent, foster_carer=foster_carer)
                if children.exists():
                    serializer = ParentSerializer(parent)
                    return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            foster_carer = FosterCarer.objects.get(id=request.user.id)
            children = Child.objects.filter(foster_carer=foster_carer)
            parents = Parent.objects.filter(gender=gender)
            ret = []

            for child in children:
                for parent in parents:
                    if child.mother.id == parent.id or child.father.id == parent.id:
                        ret.append(parent)


            if ret != []:
                serializer = ParentSerializer(ret, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
    
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
            gender = request.data.get('gender')
            if gender in ['M', 'F']:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Invalid gender. Gender must be 'M' for mother or 'F' for father."},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, gender=None, parent_id=None, *args, **kwargs):
        """
        Updates an existing parent by ID.

        Parameters:
        - request: The request object.
        - gender (optional): The gender of the parent to update ('M' for mother, 'F' for father).
        - parent_id: The ID of the parent to update.

        Returns:
        - Response: The serialized data of the updated parent.
        """
        if parent_id:
            parent = Parent.objects.get(id=parent_id)
            foster_carer = FosterCarer.objects.get(id=request.user.id)

            if parent.gender == gender:
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

    def delete(self, request, gender, parent_id, *args, **kwargs):
        """
        Deletes a parent by ID.

        Parameters:
        - request: The request object.
        - gender: The gender of the parent to delete ('M' for mother, 'F' for father).
        - parent_id: The ID of the parent to delete.

        Returns:
        - Response: A success status indicating the deletion.
        """
        parent = Parent.objects.get(id=parent_id)
        foster_carer = FosterCarer.objects.get(id=request.user.id)

        if parent.gender == gender:
            if parent.gender == 'M':
                children = Child.objects.filter(foster_carer=foster_carer, mother=parent)
            else:
                children = Child.objects.filter(foster_carer=foster_carer, father=parent)

            if children.exists():
                parent.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
