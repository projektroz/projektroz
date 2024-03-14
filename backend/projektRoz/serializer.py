from rest_framework import serializers
from .models import Mother, Father, Notes, Address, FosterCarer, AddressRegistered, Child, Siblings, Category, Documents

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
    Serializer class for the FosterCarer model.

    This serializer is used to convert FosterCarer model instances into JSON
    representation and vice versa. It specifies all the fields of the FosterCarer
    model to be included in the serialized output.

    Attributes:
        model: The model class that the serializer is based on.
        fields: A string or list of strings specifying the fields to include in the
                serialized output. In this case, "__all__" is used to include all
                fields of the FosterCarer model.

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

