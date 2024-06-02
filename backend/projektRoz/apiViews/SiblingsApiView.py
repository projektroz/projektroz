from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from projektRoz.models import Siblings, FosterCarer, Child
from projektRoz.serializer import SiblingsSerializer

class SiblingsApiView(APIView):
    """
    API view for managing siblings.
    """

    permission_classes = [permissions.IsAuthenticated]
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('siblings_id', openapi.IN_QUERY, description="ID of the siblings", type=openapi.TYPE_INTEGER)
        ],
        responses={200: SiblingsSerializer(many=True), 404: 'Not Found'}
    )
    def get(self, request, siblings_id = None, *args, **kwargs):
        """
        Retrieve siblings.

        Args:
            request (HttpRequest): The request object.
            siblings_id (int, optional): The ID of the siblings to retrieve. Defaults to None.

        Returns:
            Response: The response object containing the serialized siblings data.
        """
        if siblings_id:
            siblings = Siblings.objects.get(id = siblings_id)
            child = siblings.child
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            if child.foster_carer == fosterCarer:
                serializer = SiblingsSerializer(siblings, many = False)

                return Response(serializer.data, status=status.HTTP_200_OK)
            
        else:
            fosterCarer = FosterCarer.objects.get(id = request.user.id)
            siblings = Siblings.objects.all()
            ret = []

            for i in siblings:
                if i.child.foster_carer == fosterCarer:
                    ret.append(i)
            
            if ret != []:
                serializer = SiblingsSerializer(ret, many = True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=SiblingsSerializer,
        responses={201: SiblingsSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new sibling.

        Args:
            request (HttpRequest): The request object.

        Returns:
            Response: The response object containing the serialized sibling data if successful, 
                      or the error message if validation fails.
        """
        serializer = SiblingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=SiblingsSerializer,
        responses={200: SiblingsSerializer, 404: 'Not Found', 400: 'Bad Request'}
    )
    def put(self, request, siblings_id = None, *args, **kwargs):
        """
        Update an existing sibling.

        Args:
            request (HttpRequest): The request object.
            siblings_id (int): The ID of the sibling to update.

        Returns:
            Response: The response object containing the serialized sibling data if successful, 
                      or the error message if validation fails.
        """
        
        if siblings_id:
            siblings = Siblings.objects.get(id = siblings_id)
            child = siblings.child
            fosterCarer = FosterCarer.objects.get(id = request.user.id)

            if child.foster_carer == fosterCarer:
                serializer = SiblingsSerializer(siblings, data = request.data)
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                    
        # else:
        #     siblings = Siblings.objects.get(id = siblings_id)
        #     child = siblings.child
        #     fosterCarer = FosterCarer.objects.get(id = request.user.id)

        #     if child.foster_carer == fosterCarer:
        #         serializer = SiblingsSerializer(siblings, data = request.data)
        #         if serializer.is_valid():
        #             serializer.save()

        #             return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, siblings_id, *args, **kwargs):
        """
        Delete a sibling.

        Args:
            request (HttpRequest): The request object.
            siblings_id (int): The ID of the sibling to delete.

        Returns:
            Response: The response object with no content if successful, or the error message if the sibling is not found.
        """

        siblings = Siblings.objects.get(id=siblings_id)
        child = siblings.child
        fosterCarer = FosterCarer.objects.get(id = request.user.id)

        if child.foster_carer == fosterCarer:
            siblings.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        