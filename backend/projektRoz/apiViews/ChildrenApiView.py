from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from projektRoz.models import Child, FosterCarer
from projektRoz.serializer import ChildSerializer


class ChildrenApiView(APIView):
    """API view for managing child objects.

    Attributes:
        permission_classes (list): List of permission classes for the view.

    Methods:
        get: Retrieve a list of child objects or a specific child object.
        post: Create a new child object.
        put: Update an existing child object.
        delete: Delete a child object.
    """

    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "child_id",
                openapi.IN_QUERY,
                description="ID of the child",
                type=openapi.TYPE_INTEGER,
            )
        ],
        responses={200: ChildSerializer(many=True), 404: "Not Found"},
    )
    def get(self, request, child_id=None, *args, **kwargs):
        """Retrieve a list of child objects or a specific child object.

        Args:
            request (HttpRequest): The HTTP request object.
            child_id (int, optional): The ID of the child object to retrieve. Defaults to None.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized child object(s).

        Raises:
            None
        """

        try:
            foster_carer = FosterCarer.objects.get(user=request.user.id)
        except FosterCarer.DoesNotExist:
            return Response(
                {"error": "Foster carer not found for this user."},
                status=status.HTTP_404_NOT_FOUND,
            )

        children = Child.objects.filter(foster_carer=foster_carer)

        if child_id:
            children = Child.objects.filter(id=child_id, foster_carer=foster_carer)

        serializer = ChildSerializer(children, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ChildSerializer,
        responses={201: ChildSerializer, 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        """Create a new child object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized child object if successful,
            or the error message if the serializer is invalid.

        Raises:
            None
        """
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            try:
                foster_carer = FosterCarer.objects.get(user=request.user)
            except FosterCarer.DoesNotExist:
                return Response(
                    {"error": "Foster Carer not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer.save(foster_carer=foster_carer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=ChildSerializer,
        responses={200: ChildSerializer, 404: "Not Found", 400: "Bad Request"},
    )
    def put(self, request, child_id, *args, **kwargs):
        """Update an existing child object.

        Args:
            request (HttpRequest): The HTTP request object.
            child_id (int): The ID of the child object to update.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized updated child object if successful,
            or the error message if the serializer is invalid.

        Raises:
            None
        """
        fosterCarer = FosterCarer.objects.get(user=request.user)
        child = Child.objects.get(id=child_id, foster_carer=fosterCarer)

        if child is not None:
            serializer = ChildSerializer(child, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

        elif child is None:
            serializer = ChildSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(foster_carer=fosterCarer)

                return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: "No Content", 404: "Not Found"})
    def delete(self, request, child_id, *args, **kwargs):
        """Delete a child object.

        Args:
            request (HttpRequest): The HTTP request object.
            child_id (int): The ID of the child object to be deleted.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object indicating the success or failure of the deletion.

        Raises:
            None
        """
        fosterCarer = FosterCarer.objects.get(user=request.user)
        child = Child.objects.get(id=child_id, foster_carer=fosterCarer)

        if child is not None:
            child.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
