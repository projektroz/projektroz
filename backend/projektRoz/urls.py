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

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    
    path("children/api", ChildrenApiView.as_view(), name="children"),
    path('children/api/<int:child_id>/', ChildrenApiView.as_view(), name='children'),
    
    path("mother/api", MotherApiView.as_view(), name="mother"),
    path('mother/api/<int:mother_id>/', MotherApiView.as_view(), name='mother'),
    
    path("father/api", FatherApiView.as_view(), name="father"),
    path('father/api/<int:father_id>/', FatherApiView.as_view(), name='father'),
    
    path("notes/api", NotesApiView.as_view(), name="notes"),
    path('notes/api/<int:note_id>/', NotesApiView.as_view(), name='notes'),
    
    path("address/api", AddressApiView.as_view(), name="address"),
    path('address/api/<int:address_id>/', AddressApiView.as_view(), name='address'),
    
    path("foster_carer/api", FosterCarerApiView.as_view(), name="foster_carer"),
    path('foster_carer/api/<int:foster_carer_id>/', FosterCarerApiView.as_view(), name='foster_carer'),
    
    path("address_registered/api", AddressRegisteredApiView.as_view(), name="address_registered"),
    path('address_registered/api/<int:address_registered_id>/', AddressRegisteredApiView.as_view(), name='address_registered'),
    
    path("siblings/api", SiblingsApiView.as_view(), name="siblings"),
    path('siblings/api/<int:siblings_id>/', SiblingsApiView.as_view(), name='siblings'),
    
    path("category/api", CategoryApiView.as_view(), name="category"),
    path('category/api/<int:category_id>/', CategoryApiView.as_view(), name='category'),
    
    path("documents/api", DocumentsApiView.as_view(), name="documents"),
    path('documents/api/<int:documents_id>/', DocumentsApiView.as_view(), name='documents'),
    
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]