from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from projektRoz.models import Mother, Child, FosterCarer
from projektRoz.serializer import MotherSerializer

class MotherApiView(APIView):
    """
    API view for interacting with the Mother model.

    Methods:
    - get: Retrieves a list of all mothers or a specific mother by ID.
    - post: Creates a new mother.
    - put: Updates an existing mother by ID.
    - delete: Deletes a mother by ID.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, mother_id = None, *args, **kwargs):
        """
        Retrieves a list of all mothers or a specific mother by ID.

        Parameters:
        - request: The request object.
        - mother_id (optional): The ID of the mother to retrieve.

        Returns:
        - Response: The serialized data of the mother(s).
        """
        if mother_id:
            mother = Mother.objects.get(id=mother_id)
            children = Child.objects.filter(mother = mother)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            for child in children:
                if child.foster_carer == fosterCarer:
                    serializer = MotherSerializer(mother, many = False)

                    return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            children = Child.objects.filter(foster_carer = fosterCarer)
            mothers = Mother.objects.all()
            ret = []

            for child in children:
                for mother in mothers:
                    if child.mother == mother:
                        ret.append(mother)

            if ret != []:
                serializer = MotherSerializer(ret, many = True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        """
        Creates a new mother.

        Parameters:
        - request: The request object.

        Returns:
        - Response: The serialized data of the created mother.
        """
        serializer = MotherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, mother_id = None, *args, **kwargs):
        """
        Updates an existing mother by ID.

        Parameters:
        - request: The request object.
        - mother_id: The ID of the mother to update.

        Returns:
        - Response: The serialized data of the updated mother.
        """
        if mother_id:
            mother = Mother.objects.get(id=mother_id)
            children = Child.objects.filter(mother = mother)
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            for child in children:
                if child.foster_carer == fosterCarer:
                    serializer = MotherSerializer(mother, data = request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            serializer = MotherSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, mother_id, *args, **kwargs):
        """
        Deletes a mother by ID.

        Parameters:
        - request: The request object.
        - mother_id: The ID of the mother to delete.

        Returns:
        - Response: A success status indicating the deletion.
        """
        mother = Mother.objects.get(id=mother_id)
        children = Child.objects.filter(mother = mother)
        fosterCarer = FosterCarer.objects.get(id = request.user.id)

        for child in children:
            if child.foster_carer == fosterCarer:
                mother.delete()
                    
                return Response(status=status.HTTP_204_NO_CONTENT)
            
        return Response(status=status.HTTP_404_NOT_FOUND)