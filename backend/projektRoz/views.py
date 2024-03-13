from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import (
    Child, 
    Mother, 
    Father, 
    Notes, 
    Address, 
    FosterCarer, 
    AddressRegistered, 
    Siblings, 
    Category, 
    Documents,
    )
from .serializer import (
    ChildSerializer, 
    MotherSerializer, 
    FatherSerializer, 
    NotesSerializer,
    AddressSerializer,
    FosterCarerSerializer,
    AddressRegisteredSerializer,
    SiblingsSerializer,
    CategorySerializer,
    DocumentsSerializer,
    )


class ChildrenApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, child_id = None, *args, **kwargs):
        if child_id is None:
            children = Child.objects.all().order_by('id')
        else:
            children = Child.objects.filter(id = child_id)
        serializer = ChildSerializer(children, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = ChildSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, child_id, *args, **kwargs):
        child = Child.objects.get(id = child_id)
        
        if child is not None:
            serializer = ChildSerializer(child, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif child is None:
            serializer = ChildSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, child_id, *args, **kwargs):
        child = Child.objects.get(id = child_id)
        
        if child is not None:
            child.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class MotherApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, mother_id = None, *args, **kwargs):
        if mother_id is None:
            mother = Mother.objects.all().order_by('id')
        else:
            mother = Mother.objects.filter(id = mother_id)
            
        serializer = MotherSerializer(mother, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = MotherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, mother_id, *args, **kwargs):
        mother = Mother.objects.get(id = mother_id)
        
        if mother is not None:
            serializer = MotherSerializer(mother, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif mother is None:
            serializer = MotherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, mother_id, *args, **kwargs):
        mother = Mother.objects.get(id = mother_id)
        
        if mother is not None:
            mother.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class FatherApiView(APIView):
        permission_classes = [permissions.IsAuthenticated]
        
        def get(self, request, father_id = None, *args, **kwargs):
            if father_id is None:
                father = Father.objects.all().order_by('id')
            else:
                father = Father.objects.filter(id = father_id)
                
            serializer = FatherSerializer(father, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def post(self, request, *args, **kwargs):
            serializer = FatherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def put(self, request, father_id, *args, **kwargs):
            father = Father.objects.get(id = father_id)
            
            if father is not None:
                serializer = FatherSerializer(father, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_200_OK)
            
            elif father is None:
                serializer = FatherSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, father_id, *args, **kwargs):
            father = Father.objects.get(id = father_id)
            
            if father is not None:
                father.delete()
                
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

class NotesApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, note_id = None, *args, **kwargs):
        if note_id is None:
            note = Notes.objects.all().order_by('id')
        else:
            note = Notes.objects.filter(id = note_id)
            
        serializer = NotesSerializer(note, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, note_id, *args, **kwargs):
        note = Notes.objects.get(id = note_id)
        
        if note is not None:
            serializer = NotesSerializer(note, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif note is None:
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, note_id, *args, **kwargs):
        note = Notes.objects.get(id = note_id)
        
        if note is not None:
            note.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class AddressApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, address_id = None, *args, **kwargs):
        if address_id is None:
            address = Address.objects.all().order_by('id')
        else:
            address = Address.objects.filter(id = address_id)
            
        serializer = AddressSerializer(address, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, address_id, *args, **kwargs):
        address = Address.objects.get(id = address_id)
        
        if address is not None:
            serializer = AddressSerializer(address, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif address is None:
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, address_id, *args, **kwargs):
        address = Address.objects.get(id = address_id)
        
        if address is not None:
            address.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class FosterCarerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, foster_career_id = None, *args, **kwargs):
        if foster_career_id is None:
            foster_career = FosterCarer.objects.all().order_by('id')
        else:
            foster_career = FosterCarer.objects.filter(id = foster_career_id)
            
        serializer = FosterCarerSerializer(foster_career, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = FosterCarerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, foster_career_id, *args, **kwargs):
        foster_career = FosterCarer.objects.get(id = foster_career_id)
        
        if foster_career is not None:
            serializer = FosterCarerSerializer(foster_career, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif foster_career is None:
            serializer = FosterCarerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, foster_career_id, *args, **kwargs):
        foster_career = FosterCarer.objects.get(id = foster_career_id)
        
        if foster_career is not None:
            foster_career.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AddressRegisteredApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, address_registered_id = None, *args, **kwargs):
        if address_registered_id is None:
            address_registered = AddressRegistered.objects.all().order_by('id')
        else:
            address_registered = AddressRegistered.objects.filter(id = address_registered_id)
            
        serializer = AddressRegisteredSerializer(address_registered, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = AddressRegisteredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, address_registered_id, *args, **kwargs):
        address_registered = AddressRegistered.objects.get(id = address_registered_id)
        
        if address_registered is not None:
            serializer = AddressRegisteredSerializer(address_registered, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif address_registered is None:
            serializer = AddressRegisteredSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, address_registered_id, *args, **kwargs):
        address_registered = AddressRegistered.objects.get(id = address_registered_id)
        
        if address_registered is not None:
            address_registered.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class SiblingsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, siblings_id = None, *args, **kwargs):
        if siblings_id is None:
            siblings = Siblings.objects.all().order_by('id')
        else:
            siblings = Siblings.objects.filter(id = siblings_id)
            
        serializer = SiblingsSerializer(siblings, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = SiblingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, siblings_id, *args, **kwargs):
        siblings = Siblings.objects.get(id = siblings_id)
        
        if siblings is not None:
            serializer = SiblingsSerializer(siblings, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif siblings is None:
            serializer = SiblingsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, siblings_id, *args, **kwargs):
        siblings = Siblings.objects.get(id = siblings_id)
        
        if siblings is not None:
            siblings.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class CategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, category_id = None, *args, **kwargs):
        if category_id is None:
            category = Category.objects.all().order_by('id')
        else:
            category = Category.objects.filter(id = category_id)
            
        serializer = CategorySerializer(category, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, category_id, *args, **kwargs):
        category = Category.objects.get(id = category_id)
        
        if category is not None:
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif category is None:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, category_id, *args, **kwargs):
        category = Category.objects.get(id = category_id)
        
        if category is not None:
            category.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DocumentsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, document_id = None, *args, **kwargs):
        if document_id is None:
            document = Documents.objects.all().order_by('id')
        else:
            document = Documents.objects.filter(id = document_id)
            
        serializer = DocumentsSerializer(document, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, document_id, *args, **kwargs):
        document = Documents.objects.get(id = document_id)
        
        if document is not None:
            serializer = DocumentsSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif document is None:
            serializer = DocumentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, document_id, *args, **kwargs):
        document = Documents.objects.get(id = document_id)
        
        if document is not None:
            document.delete()
            
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

def index(request):
    return HttpResponse("Hello, world. You're at the projektroz index.")