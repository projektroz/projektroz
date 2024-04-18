from django.urls import path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apiViews.RegistrationView import RegistrationView
from projektRoz.apiViews import (
    AddressApiView,
    ChildrenApiView,
    MotherApiView,
    FatherApiView,
    NotesApiView,
    FosterCarerApiView,
    AddressRegisteredApiView,
    SiblingsApiView,
    CategoryApiView,
    DocumentsApiView,
    
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Detailed documentation of all API endpoints in the projektRoz",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    
    path('api/children/', ChildrenApiView.as_view(), name='children'),
    path('api/children/<int:child_id>', ChildrenApiView.as_view(), name='children'),
    
    path('api/mother/', MotherApiView.as_view(), name='mother'),
    path('api/mother/<int:mother_id>', MotherApiView.as_view(), name='mother'),
    
    path('api/father/', FatherApiView.as_view(), name='father'),
    path('api/father/<int:father_id>', FatherApiView.as_view(), name='father'),
    
    path('api/notes/', NotesApiView.as_view(), name='notes'),
    path('api/notes/<int:note_id>', NotesApiView.as_view(), name='notes'),
    
    path('api/address/', AddressApiView.as_view(), name='address'),
    path('api/address/<int:address_id>', AddressApiView.as_view(), name='address'),
    
    path('api/foster_carer/', FosterCarerApiView.as_view(), name='foster_carer'),
    path('api/foster_carer/<int:foster_carer_id>', FosterCarerApiView.as_view(), name='foster_carer'),
    
    path('api/address_registered/', AddressRegisteredApiView.as_view(), name='address_registered'),
    path('api/address_registered/<int:address_registered_id>', AddressRegisteredApiView.as_view(), name='address_registered'),
    
    path('api/siblings/', SiblingsApiView.as_view(), name='siblings'),
    path('api/siblings/<int:siblings_id>', SiblingsApiView.as_view(), name='siblings'),
    
    path('api/category/', CategoryApiView.as_view(), name='category'),
    path('api/category/<int:category_id>', CategoryApiView.as_view(), name='category'),
    
    path('api/documents/', DocumentsApiView.as_view(), name='documents'),
    path('api/documents/<int:document_id>', DocumentsApiView.as_view(), name='documents'),
    
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]