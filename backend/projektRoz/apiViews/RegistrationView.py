from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer import UserRegistrationSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegistrationView(APIView):
    """
    Creates the user.
    """
    
    @swagger_auto_schema(
        request_body=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer, 400: 'Bad Request'}
    )
    def post(self, request, format='json'):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)