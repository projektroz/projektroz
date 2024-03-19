from rest_framework import serializers
from .models import Mother, Father, Notes, Address, FosterCareer, AddressRegistered, Child, Siblings, Category, Documents
from django.contrib.auth.models import User


class MotherSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Mother model.

    This serializer is used to convert the Mother model instances into JSON
    representation and vice versa. It specifies all the fields of the Mother
    model to be included in the serialized output.

    Attributes:
        Meta: A nested class that specifies the metadata for the serializer,
              including the model to be serialized and the fields to be included.

    """
    class Meta:
        model = Mother
        fields = "__all__"

class FatherSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Father model.

    This serializer is used to convert the Father model instances into JSON
    representation and vice versa. It specifies all the fields of the Father
    model to be included in the serialized output.

    Attributes:
        Meta: A nested class that specifies the metadata for the serializer,
              including the model to be serialized and the fields to be included.

    """
    class Meta:
        model = Father
        fields = "__all__"

class NotesSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Notes model.

    This serializer is used to convert Notes model instances into JSON
    representation and vice versa. It specifies the model and the fields
    to include in the serialized output.

    Attributes:
        model: The model class to serialize.
        fields: The fields to include in the serialized output. In this case,
                "__all__" is used to include all fields of the model.

    """
    class Meta:
        model = Notes
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Address model.

    Serializes the Address model fields to JSON and vice versa.

    Attributes:
        model (Address): The Address model class.
        fields (str): A string specifying the fields to include in the serialized representation.
                      In this case, "__all__" is used to include all fields.

    """
    class Meta:
        model = Address
        fields = "__all__"

class FosterCareerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the fosterCareer model.

    This serializer is used to convert fosterCareer model instances into JSON
    representation and vice versa. It specifies all the fields of the fosterCareer
    model to be included in the serialized output.

    Attributes:
        model: The model class that the serializer is based on.
        fields: A string or list of strings specifying the fields to include in the
                serialized output. In this case, "__all__" is used to include all
                fields of the fosterCareer model.

    """
    class Meta:
        model = FosterCareer
        fields = "__all__"

class AddressRegisteredSerializer(serializers.ModelSerializer):
    """
    Serializer class for the AddressRegistered model.

    This serializer is used to convert AddressRegistered model instances into JSON
    and vice versa, allowing the data to be easily rendered into the desired format.

    Attributes:
        model (AddressRegistered): The model class that the serializer is based on.
        fields (str): A string specifying the fields to include in the serialized representation.
                      In this case, "__all__" is used to include all fields.

    """
    class Meta:
        model = AddressRegistered
        fields = "__all__"

class ChildSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Child model.

    This serializer is used to convert Child model instances into JSON
    representation and vice versa. It specifies all the fields of the Child
    model to be included in the serialized output.

    Attributes:
        model: The Child model class to be serialized.
        fields: A string or list of strings specifying the fields to be
            included in the serialized output. If set to "__all__", all
            fields of the model will be included.

    """
    class Meta:
        model = Child
        fields = "__all__"

class SiblingsSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Siblings model.

    This serializer is used to convert the Siblings model instances into JSON
    representation and vice versa. It specifies the fields that should be
    included in the serialized output.

    Attributes:
        model: The model class that the serializer should be based on.
        fields: A string or list of strings specifying the fields to include in
                the serialized output. If set to "__all__", all fields of the
                model will be included.

    """
    class Meta:
        model = Siblings
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Category model.

    Serializes the Category model fields to JSON and vice versa.

    Attributes:
        model (Category): The Category model class.
        fields (str): A string specifying the fields to include in the serialized representation.
                      In this case, "__all__" is used to include all fields.

    """
    class Meta:
        model = Category
        fields = "__all__"

class DocumentsSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Documents model.

    This serializer is used to convert Documents model instances into JSON
    representation and vice versa. It specifies the model and the fields to be
    included in the serialization process.

    Attributes:
        model (class): The model class to be serialized.
        fields (str or list): The fields to be included in the serialization process.
            If set to "__all__", all fields of the model will be included.

    """
    class Meta:
        model = Documents
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
    

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value


    def validate(self, data):
        if data['password'].isdigit() or data['password'].isalpha():
            raise serializers.ValidationError({'password': 'Password must contain both letters and numbers.'})

        if data['password'].islower():
            raise serializers.ValidationError({'password': 'Password must contain at least one uppercase letter.'})
    
        if len(data['password']) < 8:
            raise serializers.ValidationError({'password': 'Password must be at least 8 characters long.'})

        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        return data


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
            'email': {'required': True, 'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }