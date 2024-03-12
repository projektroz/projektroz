from rest_framework import serializers
from .models import Mother, Father, Notes, Address, FosterCarer, AddressRegistered, Child, Siblings, Category, Documents

class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = "__all__"

class FatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Father
        fields = "__all__"

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class FosterCarerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FosterCarer
        fields = "__all__"

class AddressRegisteredSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressRegistered
        fields = "__all__"

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"

class SiblingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siblings
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = "__all__"

