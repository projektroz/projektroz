from typing import Iterable
from django.db import models
from django.contrib.auth.models import User

class Mother(models.Model):
    """
    Represents a mother in the system.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    child_id = models.IntegerField()

class Father(models.Model):
    """
    Represents a father in the system.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    child_id = models.IntegerField()

class Notes(models.Model):
    """
    Represents a note in the system.
    """
    id = models.AutoField(primary_key=True)
    create_date = models.DateField()
    modification_date = models.DateField()
    note_text = models.TextField()

class Address(models.Model):
    """
    Represents an address in the system.
    """
    id = models.AutoField(primary_key=True)
    country = models.TextField()
    city = models.TextField()
    street = models.TextField()
    postal_code = models.TextField()
    apartment_number = models.IntegerField(null=True, blank=True)

class FosterCarer(models.Model):
    """
    Represents a foster carer in the system.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.TextField(default="Noname")
    surname = models.TextField(default="Nosurname")
    email = models.EmailField(default="noemail@example.com")
    
    def save(self, *args, **kwargs) -> None:
        self.name = self.user.first_name
        self.surname = self.user.last_name
        self.email = self.user.email
        return super().save(*args, **kwargs)

class AddressRegistered(models.Model):
    """
    Represents a registered address in the system.
    """
    id = models.AutoField(primary_key=True)
    country = models.TextField()
    city = models.TextField()
    street = models.TextField()
    postal_code = models.TextField()
    apartment_number = models.IntegerField(null=True, blank=True)

class Child(models.Model):
    """
    Represents a child in the system.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.TextField(null=True, blank=True)
    pesel = models.CharField(max_length=11, null=True, unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    address_registered = models.ForeignKey(AddressRegistered, on_delete=models.CASCADE, null=True, blank=True)
    date_of_admission = models.DateField(null=True, blank=True)
    court_decision = models.CharField(max_length=30, null=True, unique=True)
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, null=True, blank=True)
    father = models.ForeignKey(Father, on_delete=models.CASCADE, null=True, blank=True)
    foster_carer = models.ForeignKey(FosterCarer, on_delete=models.CASCADE, null=True, blank=True)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE, null=True, blank=True)

class Siblings(models.Model):
    """
    Represents a sibling relationship in the system.
    """
    id = models.AutoField(primary_key=True)
    child = models.ForeignKey(Child, related_name='child', on_delete=models.CASCADE)
    child_sibling = models.ForeignKey(Child, related_name='child_sibling', on_delete=models.CASCADE)

class Category(models.Model):
    """
    Represents a category in the system.
    """
    id = models.AutoField(primary_key=True)
    category_name = models.TextField()

class Documents(models.Model):
    """
    Represents a document in the system.
    """
    id = models.AutoField(primary_key=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    document_path = models.TextField()