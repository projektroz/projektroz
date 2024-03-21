from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Father, FosterCarer, Child
from projektRoz.serializer import FatherSerializer

class FatherApiView(APIView):
    """
    API view for handling CRUD operations related to Father model.
    """

    permission_classes = [permissions.IsAuthenticated]
        
    def get(self, request, father_id = None, *args, **kwargs):
        """
        Retrieve a list of all fathers or a specific father by ID.

        Parameters:
        - request: The HTTP request object.
        - father_id (optional): The ID of the father to retrieve.

        Returns:
        - If father_id is None, returns a list of all fathers.
        - If father_id is provided, returns the specific father with the given ID.

        Raises:
        - None.
        """
        if father_id:
            father = Father.objects.get(id=father_id)
            children = Child.objects.filter(father = father)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            for child in children:
                if child.foster_carer == fosterCarer:
                    serializer = FatherSerializer(father, many = False)

                    return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            children = Child.objects.filter(foster_carer = fosterCarer)
            fathers = Father.objects.all()
            ret = []

            for child in children:
                for father in fathers:
                    if child.father == father:
                        ret.append(father)

            if ret != []:
                serializer = FatherSerializer(ret, many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        
    def post(self, request, *args, **kwargs):
        """
        Create a new father.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - If the request data is valid, returns the created father data.
        - If the request data is invalid, returns the validation errors.

        Raises:
        - None.
        """
        serializer = FatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
                
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, father_id = None, *args, **kwargs):
        """
        Update an existing father.

        Parameters:
        - request: The HTTP request object.
        - father_id: The ID of the father to update.

        Returns:
        - If the father with the given ID exists, returns the updated father data.
        - If the father with the given ID does not exist, creates a new father with the provided data.
        - If the request data is invalid, returns the validation errors.

        Raises:
        - None.
        """
        if father_id:
            father = Father.objects.get(id=father_id)
            children = Child.objects.filter(father = father)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            for child in children:
                if child.foster_carer == fosterCarer:
                    serializer = FatherSerializer(father, data = request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            serializer = FatherSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, father_id, *args, **kwargs):
        """
        Delete an existing father.

        Parameters:
        - request: The HTTP request object.
        - father_id: The ID of the father to delete.

        Returns:
        - If the father with the given ID exists, deletes the father and returns a success response.
        - If the father with the given ID does not exist, returns a not found response.

        Raises:
        - None.
        """
        father = Father.objects.get(id=father_id)
        children = Child.objects.filter(father = father)
        fosterCarer = FosterCarer.objects.get(id = request.user.id)

        for child in children:
            if child.foster_carer == fosterCarer:
                father.delete()
                    
                return Response(status=status.HTTP_204_NO_CONTENT)
                
            return Response(status=status.HTTP_404_NOT_FOUND)
