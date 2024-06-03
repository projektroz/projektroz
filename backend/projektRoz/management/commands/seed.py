from django.core.management.base import BaseCommand
from faker import Faker
from projektRoz.models import Parent, Notes, Address, FosterCarer, Child, Siblings, Documents, AllowedCategories
from random import randint
fake = Faker('pl_PL')  

"""
How to use seeder:
    Docker ps
    seek backend container id
    docker exec <backend_id> python manage.py seed
    wait :)
"""

# Nie działa, nie używać
class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_parents_notes(self):
        for _ in range(10):
            role = fake.random_element(elements=('M', 'F'))
            Parent.objects.create(
                name=fake.first_name_male() if role == 'M' else fake.first_name_female(),
                surname=fake.last_name_male() if role == 'M' else fake.last_name_female(),
                role=role
            )
            Notes.objects.create(
                create_date=fake.date(),
                modification_date=fake.date(),
                note_text=fake.paragraph(),
                child = Child.objects.all().first()
            )

    def add_addresses_foster_carers(self):
        for _ in range(5):
            Address.objects.create(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                postal_code=fake.postcode(),
                apartment_number=fake.random_int(min=1, max=100),
                is_registered=True
            )
            Address.objects.create(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                postal_code=fake.postcode(),
                apartment_number=fake.random_int(min=1, max=100),
                is_registered=False
            )
            # FosterCarer.objects.create(
            #     name=fake.first_name(),
            #     surname=fake.last_name(),
            #     email=fake.email(),
            #     password=fake.password()
            # )

    def add_children_categories_documents(self):
        addresses_registered = Address.objects.filter(is_registered=True)
        addresses_not_registered = Address.objects.filter(is_registered=False)
        mothers = Parent.objects.filter(role='M')
        fathers = Parent.objects.filter(role='F')

        for _ in range(10):
            child = Child.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                birth_date=fake.date_of_birth(),
                birth_place=fake.city(),
                pesel=fake.bothify(text='###########'),
                address=addresses_not_registered.order_by('?').first(),
                address_registered=addresses_registered.order_by('?').first(),
                date_of_admission=fake.date(),
                court_decision=fake.bothify(text='###/####'),
                mother=mothers.order_by('?').first(),
                father=fathers.order_by('?').first(),
                foster_carer=FosterCarer.objects.order_by('?').first(),
                # note=Notes.objects.order_by('?').first()
            )
            Siblings.objects.create(
                child=child,
                child_sibling=Child.objects.order_by('?').first()
            )
            # Category.objects.create(
            #     category_name=fake.word()
            # )
            Documents.objects.create(
                child=child,
                category=AllowedCategories.choices[randint(0, len(AllowedCategories.choices) - 1)][0],
                document_path=fake.file_path(depth=1)
            )

    def handle(self, *args, **options):
        self.add_parents_notes()
        self.add_addresses_foster_carers()
        self.add_children_categories_documents()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))