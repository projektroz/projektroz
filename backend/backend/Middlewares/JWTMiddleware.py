from rest_framework_simplejwt.exceptions import TokenError
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTMiddleware(MiddlewareMixin):
    def process_request(self, request):
        exempt_paths = ['/login/', '/register/', '/refresh/']
        print("chuj")
        if request.path in exempt_paths:
            return None  

        auth = JWTAuthentication()
        header = auth.get_header(request)
        
        if header is None:
            return HttpResponse('No token provided', status=406)
        
        else:
            raw_token = auth.get_raw_token(header)
            if raw_token is None or raw_token == b'':
                return HttpResponse('No token provided', status=406)

        try:
            validated_token = auth.get_validated_token(raw_token)
            request.user = auth.get_user(validated_token)
        except Exception as e:
            error_detail = str(e)
            response_data = {
                'detail': 'Token error',
                'error': error_detail
            }

            if 'token_not_valid' in str(error_detail):
                return JsonResponse(response_data, status=401)
            return JsonResponse(response_data, status=500)
        return None
