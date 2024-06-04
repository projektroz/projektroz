from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from gdstorage.storage import GoogleDriveStorage

# gd_storage = GoogleDriveStorage(json_keyfile_path='/app/projektRoz/service.json')

# class Map(models.Model):
#     id = models.AutoField(primary_key=True)
#     map_name = models.CharField(max_length=200)
#     map_data = models.FileField(upload_to='maps', storage=gd_storage)

class Person(models.Model):
    """
    Represents a person in the system.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()

    class Meta:
        abstract = True

class Parent(Person):
    """
    Represents a parent in the system.
    """
    ROLE_CHOICES = [
        ('M', 'Mother'),
        ('F', 'Father'),
    ]
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.TextField()
    city = models.TextField()
    street = models.TextField()
    postal_code = models.TextField()
    apartment_number = models.IntegerField(null=True, blank=True)
    is_registered = models.BooleanField(default=False)

class FosterCarer(models.Model):
    """
    Represents a foster carer in the system.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="Noname")
    surname = models.TextField(default="Nosurname")
    email = models.EmailField(default="noemail@example.com")
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs) -> None:
        self.name = self.user.first_name
        self.surname = self.user.last_name
        self.email = self.user.email
        return super().save(*args, **kwargs)

class Child(Person):
    """
    Represents a child in the system.
    """
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.TextField(null=True, blank=True)
    pesel = models.CharField(max_length=11, null=True, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='address')
    address_registered = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='address_registered')
    date_of_admission = models.DateField(null=True, blank=True)
    date_of_discharge = models.DateField(null=True, blank=True)
    court_decision = models.CharField(max_length=30, null=True, unique=True)
    mother = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True, related_name='mother')
    father = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True, blank=True, related_name='father')
    foster_carer = models.ForeignKey(FosterCarer, on_delete=models.CASCADE, null=True, blank=True)
    # note = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True, blank=True)

class Notes(models.Model):
    """
    Represents a note in the system.
    """
    id = models.AutoField(primary_key=True)
    create_date = models.DateField()
    modification_date = models.DateField()
    note_text = models.TextField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, blank=True)
class Siblings(models.Model):
    """
    Represents a sibling relationship in the system.
    """
    id = models.AutoField(primary_key=True)
    child = models.ForeignKey(Child, related_name='child', on_delete=models.CASCADE)
    child_sibling = models.ForeignKey(Child, related_name='child_sibling', on_delete=models.CASCADE)


class AllowedCategories(models.TextChoices):
    """
    Represents the allowed categories for a document model.
    
    """
    SZKOLA = 'Szkola'
    SAD = 'Sad'
    ZDROWIE = 'Zdrowie'
    SCHEMATY = 'Schematy'
    ZDJECIE = 'Zdjecie'
    INNE = 'Inne'

class Documents(models.Model):
    """
    Represents a document in the system.
    """

    id = models.AutoField(primary_key=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    category = models.CharField(max_length=8, choices=AllowedCategories.choices)
    document_path = models.TextField(null=True, blank=True)
    document_google_id = models.TextField(null=True, blank=True)