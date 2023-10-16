import random
from django.core.management.base import BaseCommand
from faker import Faker
from centrika.models import Transaction

fake = Faker()


class Command(BaseCommand):
    help = "Populate the database with fake transaction data"

    def add_arguments(self, parser):
        parser.add_argument(
            "count", type=int, help="Number of fake transactions to create"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for _ in range(count):
            transaction = Transaction(
                transaction_id=fake.uuid4(),
                ticket_id=fake.uuid4(),
                ticket_reference=fake.uuid4(),
                amount=random.uniform(10.0, 1000.0),
                date=fake.date_between(start_date="-30d", end_date="today"),
                time=fake.time(),
                card_id=fake.uuid4(),
                plate_number=fake.license_plate(),
                route_name=fake.company(),
                organization=fake.company(),
                status=random.choice(["Pending", "Completed", "Failed"]),
            )
            transaction.save()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {count} fake transactions")
        )
