from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

class JWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth = JWTAuthentication()
        header = auth.get_header(request)
        if header is None:
            return  

        raw_token = auth.get_raw_token(header)
        if raw_token is None:
            return 

        validated_token = auth.get_validated_token(raw_token)

        try:
            request.user = auth.get_user(validated_token)
        except AuthenticationFailed as e:
            pass
