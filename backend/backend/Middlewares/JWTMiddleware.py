from rest_framework_simplejwt.exceptions import TokenError
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTMiddleware(MiddlewareMixin):
    """
    Middleware class for JWT authentication.

    This middleware validates JWT tokens for incoming requests and sets the authenticated user in the request object.

    Attributes:
        get_response (callable): The next middleware or view function in the chain.

    Methods:
        process_request(request): Processes the incoming request and performs JWT token validation.

    """

    def __init__(self, get_response):
        self.get_response = get_response
        
    def process_request(self, request):
        """
        Processes the incoming request and performs JWT token validation.

        Args:
            request (HttpRequest): The incoming request object.

        Returns:
            None or HttpResponse or JsonResponse: Returns None if the request path is exempted from token validation.
                                                  Returns an HttpResponse with an appropriate error message if the token is missing or invalid.
                                                  Returns None if the token is valid and sets the authenticated user in the request object.

        """
        exempt_paths = ['/login/', '/register/', '/refresh/', '/swagger/', '/redoc/', '/swagger.json']

        if request.path in exempt_paths:
            return None  
        if request.path.startswith('/admin/'):
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
