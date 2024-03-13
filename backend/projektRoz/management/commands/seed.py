from django.core.management.base import BaseCommand
from faker import Faker
from projektRoz.models import Mother, Father, Notes, Address, FosterCarer, AddressRegistered, Child, Siblings, Category, Documents

fake = Faker('pl_PL')  

"""
How to use seeder:
    Docker ps
    seek backend container id
    docker exec <backend_id> python manage.py seed
    wait :)
"""


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_mothers_fathers_notes(self):
        for _ in range(5):
            Mother.objects.create(
                name=fake.first_name_female(),
                surname=fake.last_name_female(),
                child_id=fake.random_int(min=1, max=5)
            )
            Father.objects.create(
                name=fake.first_name_male(),
                surname=fake.last_name_male(),
                child_id=fake.random_int(min=1, max=5)
            )
            Notes.objects.create(
                create_date=fake.date(),
                modification_date=fake.date(),
                note_text=fake.paragraph()
            )

    def add_addresses_foster_carers(self):
        for _ in range(5):
            Address.objects.create(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                postal_code=fake.postcode(),
                apartment_number=fake.random_int(min=1, max=100)
            )
            FosterCarer.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                email=fake.email(),
                password=fake.password()
            )
            AddressRegistered.objects.create(
                country=fake.country(),
                city=fake.city(),
                street=fake.street_name(),
                postal_code=fake.postcode(),
                apartment_number=fake.random_int(min=1, max=100)
            )

    def add_children_categories_documents(self):
        for _ in range(5):
            child = Child.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                birth_date=fake.date_of_birth(),
                birth_place=fake.city(),
                pesel=fake.bothify(text='###########'),
                address=Address.objects.order_by('?').first(),
                address_registered=AddressRegistered.objects.order_by('?').first(),
                date_of_admission=fake.date(),
                court_decision=fake.bothify(text='###/####'),
                mother=Mother.objects.order_by('?').first(),
                father=Father.objects.order_by('?').first(),
                foster_career=FosterCarer.objects.order_by('?').first(),
                note=Notes.objects.order_by('?').first()
            )
            Siblings.objects.create(
                child=child,
                child_sibling=Child.objects.order_by('?').first()
            )
            Category.objects.create(
                category_name=fake.word()
            )
            Documents.objects.create(
                child=child,
                category=Category.objects.order_by('?').first(),
                document_path=fake.file_path(depth=1)
            )

    def handle(self, *args, **options):
        self.add_mothers_fathers_notes()
        self.add_addresses_foster_carers()
        self.add_children_categories_documents()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))