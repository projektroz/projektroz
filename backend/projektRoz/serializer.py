from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Address, Child, Documents, FosterCarer, Notes, Parent, Siblings


class ParentSerializer(serializers.ModelSerializer):
    """Serializer class for the Parent model.

    This serializer is used to convert the Mother model instances into JSON
    representation and vice versa. It specifies all the fields of the Mother
    model to be included in the serialized output.

    Attributes:
        Meta: A nested class that specifies the metadata for the serializer,
              including the model to be serialized and the fields to be included.
    """

    class Meta:
        """Meta class for defining metadata options for the Parent
        serializer."""

        model = Parent
        fields = "__all__"
        extra_kwargs = {"role": {"required": True}}


class NotesSerializer(serializers.ModelSerializer):
    """Serializer class for the Notes model.

    This serializer is used to convert Notes model instances into JSON
    representation and vice versa. It specifies the model and the fields
    to include in the serialized output.

    Attributes:
        model: The model class to serialize.
        fields: The fields to include in the serialized output. In this case,
                "__all__" is used to include all fields of the model.
    """

    class Meta:
        """Meta class for the Notes serializer.

        Attributes:
            model (Model): The model class associated with the serializer.
            fields (str or list): The fields to include in the serialized representation.
            extra_kwargs (dict): Additional keyword arguments for the fields.

        Example:
            class Meta:
                model = Notes
                fields = "__all__"
                extra_kwargs = {
                    "create_date": {"required": False},
                    "modification_date": {"required": False},
                    "note_text": {"required": True},
                    "child": {"required": True},
                }
        """

        model = Notes
        fields = "__all__"
        extra_kwargs = {
            "create_date": {"required": False},
            "modification_date": {"required": False},
            "note_text": {"required": True},
            "child": {"required": True},
        }


class AddressSerializer(serializers.ModelSerializer):
    """Serializer class for the Address model.

    Serializes the Address model fields to JSON and vice versa.

    Attributes:
        model (Address): The Address model class.
        fields (str): A string specifying the fields to include in the serialized representation.
                      In this case, "__all__" is used to include all fields.
    """

    class Meta:
        """Meta class for defining metadata options for the Address serializer.

        Attributes:
            model (Model): The model class associated with the serializer.
            fields (str or list): The fields to include in the serialized representation.
            extra_kwargs (dict): Additional keyword arguments for controlling field behavior.
        """

        model = Address
        fields = "__all__"
        extra_kwargs = {
            "country": {"required": True},
            "city": {"required": True},
            "street": {"required": True},
            "postal_code": {"required": True},
            "apartment_number": {"required": False},
            "is_registered": {"required": False},
        }


class FosterCarerSerializer(serializers.ModelSerializer):
    """Serializer class for the fosterCarer model.

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
        """Meta class for defining metadata options for the FosterCarer
        serializer.

        Attributes:
            model (Model): The model class associated with the serializer.
            fields (str or list): The fields to include in the serialized representation.
                If set to "__all__", all fields of the model will be included.
            extra_kwargs (dict): Additional keyword arguments to customize field-level behavior.
                Each key represents a field name, and the corresponding value is a dictionary
                of options for that field.
        """

        model = FosterCarer
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "surname": {"required": True},
            "email": {"required": True},
            "address": {"required": True},
        }


class ChildSerializer(serializers.ModelSerializer):
    """Serializer class for the Child model.

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
    address_registered = AddressSerializer()
    mother = ParentSerializer()
    father = ParentSerializer()

    class Meta:
        """Meta class for the Child serializer.

        Defines the metadata options for the serializer, such as the model to be serialized,
        the fields to include, and any extra kwargs for specific fields.

        Attributes:
            model (Model): The model class to be serialized.
            fields (str or list): The fields to include in the serialized representation.
                If set to "__all__", all fields of the model will be included.
            extra_kwargs (dict): Additional keyword arguments for specific fields.
                The keys are the field names, and the values are dictionaries of
                additional options for the field.

        Example:
            class Meta:
                model = Child
                fields = "__all__"
                extra_kwargs = {
                    "name": {"required": True},
                    "surname": {"required": True},
                    "birth_date": {"required": True},
                    "birth_place": {"required": True},
                    "pesel": {"required": True},
                    "date_of_admission": {"required": True},
                    "court_decision": {"required": True},
                    "address": {"required": True},
                    "address_registered": {"required": True},
                    "mother": {"required": True},
                    "father": {"required": True},
                }
        """

        model = Child
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": True},
            "surname": {"required": True},
            "birth_date": {"required": True},
            "birth_place": {"required": True},
            "pesel": {"required": True},
            "date_of_admission": {"required": True},
            "court_decision": {"required": True},
            "address": {"required": True},
            "address_registered": {"required": True},
            "mother": {"required": True},
            "father": {"required": True},
        }

    def create(self, validated_data):
        """Create a new child object with the provided validated data.

        Args:
            validated_data (dict): The validated data for creating the child object.

        Returns:
            Child: The newly created child object.
        """
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)

        address_registered_data = validated_data.pop("address_registered")
        address_registered = Address.objects.create(**address_registered_data)

        mother_data = validated_data.pop("mother")
        mother = Parent.objects.create(**mother_data)

        father_data = validated_data.pop("father")
        father = Parent.objects.create(**father_data)

        child = Child.objects.create(
            address=address,
            address_registered=address_registered,
            father=father,
            mother=mother,
            **validated_data
        )

        return child

    def update(self, instance, validated_data):
        """Updates the instance with the provided validated data.

        Args:
            instance: The instance to be updated.
            validated_data: The validated data containing the updated values.

        Returns:
            The updated instance.
        """
        address_data = validated_data.pop("address")
        address = instance.address
        address.country = address_data.get("country", address.country)
        address.street = address_data.get("street", address.street)
        address.city = address_data.get("city", address.city)
        address.postal_code = address_data.get("postal_code", address.postal_code)
        address.apartment_number = address_data.get(
            "apartment_number", address.apartment_number
        )
        address.save()

        address_registered_data = validated_data.pop("address_registered")
        address_registered = instance.address_registered
        address_registered.country = address_registered_data.get(
            "country", address_registered.country
        )
        address_registered.street = address_registered_data.get(
            "street", address_registered.street
        )
        address_registered.city = address_registered_data.get(
            "city", address_registered.city
        )
        address_registered.postal_code = address_registered_data.get(
            "postal_code", address_registered.postal_code
        )
        address_registered.apartment_number = address_registered_data.get(
            "apartment_number", address_registered.apartment_number
        )
        address_registered.save()

        mother_data = validated_data.pop("mother")
        mother = instance.mother
        mother.name = mother_data.get("name", mother.name)
        mother.surname = mother_data.get("surname", mother.surname)
        mother.role = mother_data.get("role", mother.role)
        mother.save()

        father_data = validated_data.pop("father")
        father = instance.father
        father.name = father_data.get("name", father.name)
        father.surname = father_data.get("surname", father.surname)
        father.role = father_data.get("role", father.role)
        father.save()

        instance.name = validated_data.get("name", instance.name)
        instance.surname = validated_data.get("surname", instance.surname)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.birth_place = validated_data.get("birth_place", instance.birth_place)
        instance.pesel = validated_data.get("pesel", instance.pesel)
        instance.date_of_admission = validated_data.get(
            "date_of_admission", instance.date_of_admission
        )
        instance.court_decision = validated_data.get(
            "court_decision", instance.court_decision
        )

        instance.save()

        return instance


class SiblingsSerializer(serializers.ModelSerializer):
    """Serializer class for the Siblings model.

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
        """Meta class for the Siblings serializer.

        Defines the metadata options for the serializer, such as the
        model to be serialized, the fields to include, and any extra
        kwargs.
        """

        model = Siblings
        fields = "__all__"
        extra_kwargs = {"child": {"required": True}}


class DocumentsSerializer(serializers.ModelSerializer):
    """Serializer class for the Documents model.

    This serializer is used to convert Documents model instances into JSON
    representation and vice versa. It specifies the model and the fields to be
    included in the serialization process.

    Attributes:
        model (class): The model class to be serialized.
        fields (str or list): The fields to be included in the serialization process.
            If set to "__all__", all fields of the model will be included.
    """

    class Meta:
        """Meta class for the Documents serializer.

        This class provides additional options and configurations for
        the serializer.
        """

        model = Documents
        fields = "__all__"
        extra_kwargs = {
            "child": {"required": True},
            "category": {"required": True},
            "document_path": {"required": True},
            "document_google_id": {"required": True},
        }


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for the User model."""

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """Create and return a new User instance.

        Args:
            validated_data (dict): Validated data for creating a new User.

        Returns:
            User: The created User instance.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer class for user registration.

    This serializer is used to validate and serialize user registration data.
    It performs various validations on the input data, such as checking for
    existing email, password strength, and matching password fields.

    Attributes:
        passwordRepeat (CharField): A write-only field for password confirmation.

    Methods:
        create(validated_data): Creates a new user instance based on the validated data.
        validate_email(value): Validates the uniqueness of the email field.
        validate(data): Performs additional validations on the input data.

    Meta:
        model (User): The User model to be used for serialization.
        fields (list): The fields to be included in the serialized output.
        extra_kwargs (dict): Additional keyword arguments for field customization.
    """

    passwordRepeat = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    def create(self, validated_data):
        """Create a new user instance with the provided validated data.

        Args:
            validated_data (dict): A dictionary containing the validated data for creating a new user.

        Returns:
            User: The newly created user instance.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user

    def validate_email(self, value):
        """Validates the email field to ensure it is unique.

        Args:
            value (str): The email value to be validated.

        Raises:
            serializers.ValidationError: If the email already exists in the User model.

        Returns:
            str: The validated email value.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate(self, data):
        """Validates the input data for password.

        Args:
            data (dict): The input data containing the password and passwordRepeat fields.

        Raises:
            serializers.ValidationError: If the password does not meet the validation criteria.

        Returns:
            dict: The validated data.
        """
        if data["password"].isdigit() or data["password"].isalpha():
            raise serializers.ValidationError(
                {"password": "Password must contain both letters and numbers."}
            )

        if data["password"].islower():
            raise serializers.ValidationError(
                {"password": "Password must contain at least one uppercase letter."}
            )

        if len(data["password"]) < 8:
            raise serializers.ValidationError(
                {"password": "Password must be at least 8 characters long."}
            )

        if data["password"] != data["passwordRepeat"]:
            raise serializers.ValidationError({"password": "Passwords must match."})

        return data

    class Meta:
        """Meta class for defining metadata options for the UserSerializer
        class.

        Attributes:
            model (Model): The model class associated with the serializer.
            fields (list): The list of fields to include in the serialized representation.
            extra_kwargs (dict): Additional keyword arguments for controlling field behavior.
        """

        model = User
        fields = [
            "username",
            "password",
            "passwordRepeat",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "passwordRepeat": {"write_only": True},
            "email": {"required": True, "write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }
