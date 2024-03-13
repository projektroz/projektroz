from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    
    path("children/api", views.ChildrenApiView.as_view(), name="children"),
    path('children/api/<int:child_id>/', views.ChildrenApiView.as_view(), name='children'),
    
    path("mother/api", views.MotherApiView.as_view(), name="mother"),
    path('mother/api/<int:mother_id>/', views.MotherApiView.as_view(), name='mother'),
    
    path("father/api", views.FatherApiView.as_view(), name="father"),
    path('father/api/<int:father_id>/', views.FatherApiView.as_view(), name='father'),
    
    path("notes/api", views.NotesApiView.as_view(), name="notes"),
    path('notes/api/<int:note_id>/', views.NotesApiView.as_view(), name='notes'),
    
    path("address/api", views.AddressApiView.as_view(), name="address"),
    path('address/api/<int:address_id>/', views.AddressApiView.as_view(), name='address'),
    
    path("foster_carer/api", views.FosterCarerApiView.as_view(), name="foster_carer"),
    path('foster_carer/api/<int:foster_carer_id>/', views.FosterCarerApiView.as_view(), name='foster_carer'),
    
    path("address_registered/api", views.AddressRegisteredApiView.as_view(), name="address_registered"),
    path('address_registered/api/<int:address_registered_id>/', views.AddressRegisteredApiView.as_view(), name='address_registered'),
    
    path("siblings/api", views.SiblingsApiView.as_view(), name="siblings"),
    path('siblings/api/<int:siblings_id>/', views.SiblingsApiView.as_view(), name='siblings'),
    
    path("category/api", views.CategoryApiView.as_view(), name="category"),
    path('category/api/<int:category_id>/', views.CategoryApiView.as_view(), name='category'),
    
    path("documents/api", views.DocumentsApiView.as_view(), name="documents"),
    path('documents/api/<int:documents_id>/', views.DocumentsApiView.as_view(), name='documents'),
    
]