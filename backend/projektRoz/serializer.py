from rest_framework import serializers
from .models import Mother, Father, Notes, Address, FosterCarer, AddressRegistered, Child, Siblings, Category, Documents
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

class FosterCarerSerializer(serializers.ModelSerializer):
    """
    Serializer class for the fosterCarer model.

    This serializer is used to convert fosterCarer model instances into JSON
    representation and vice versa. It specifies all the fields of the fosterCarer
    model to be included in the serialized output.

    Attributes:
        model: The model class that the serializer is based on.
        fields: A string or list of strings specifying the fields to include in the
                serialized output. In this case, "__all__" is used to include all
                fields of the fosterCarer model.

    """
    class Meta:
        model = FosterCarer
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
    
    address = AddressSerializer()
    address_registered = AddressRegisteredSerializer()
    mother = MotherSerializer()
    father = FatherSerializer()
    
    class Meta:
        model = Child
        fields = "__all__"
        
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        
        address_registered_data = validated_data.pop('address_registered')
        address_registered = AddressRegistered.objects.create(**address_registered_data)
        
        mother_data = validated_data.pop('mother')
        mother = Mother.objects.create(**mother_data)
        
        father_data = validated_data.pop('father')
        father = Father.objects.create(**father_data)
        
        child = Child.objects.create(
            address=address, address_registered=address_registered, father = father, mother = mother, **validated_data)
        
        return child
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address = instance.address
        address.country = address_data.get('country', address.country)
        address.street = address_data.get('street', address.street)
        address.city = address_data.get('city', address.city)
        address.postal_code = address_data.get('postal_code', address.postal_code)
        address.apartment_number = address_data.get('apartment_number', address.apartment_number)
        address.save()
        
        address_registered_data = validated_data.pop('address_registered')
        address_registered = instance.address_registered
        address_registered.country = address_registered_data.get('country', address_registered.country)
        address_registered.street = address_registered_data.get('street', address_registered.street)
        address_registered.city = address_registered_data.get('city', address_registered.city)
        address_registered.postal_code = address_registered_data.get('postal_code', address_registered.postal_code)
        address_registered.apartment_number = address_registered_data.get('apartment_number', address_registered.apartment_number)
        address_registered.save()
        
        mother_data = validated_data.pop('mother')
        mother = instance.mother
        mother.name = mother_data.get('name', mother.name)
        mother.surname = mother_data.get('surname', mother.surname)
        mother.save()
        
        father_data = validated_data.pop('father')
        father = instance.father
        father.name = father_data.get('name', father.name)
        father.surname = father_data.get('surname', father.surname)
        father.save()
        
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.birth_place = validated_data.get('birth_place', instance.birth_place)
        instance.pesel = validated_data.get('pesel', instance.pesel)
        instance.date_of_admission = validated_data.get('date_of_admission', instance.date_of_admission)
        instance.court_decision = validated_data.get('court_decision', instance.court_decision)

        instance.save()

        return instance
        
        

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
    passwordRepeat = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

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

        if data['password'] != data['passwordRepeat']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        
        return data


    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'passwordRepeat', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'passwordRepeat': {'write_only': True},
            'email': {'required': True, 'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }