import random
from django.utils import timezone
from faker import Faker
from .models import Transaction

fake = Faker()


def generate_fake_transaction_data():
    for _ in range(
        100
    ):  # Change this number to the desired number of fake transactions
        transaction = Transaction(
            transaction_id=fake.uuid4(),
            ticket_id=fake.uuid4(),
            ticket_reference=fake.uuid4(),
            amount=random.uniform(10.0, 1000.0),  # Adjust the range for your amount
            date=fake.date_between(
                start_date="-30d", end_date="today"
            ),  # Generate dates within the last 30 days
            time=fake.time(),
            card_id=fake.uuid4(),
            plate_number=fake.license_plate(),
            route_name=fake.company(),
            organization=fake.company(),
            status=random.choice(["Pending", "Completed", "Failed"]),
        )
        transaction.save()


if __name__ == "__main__":
    generate_fake_transaction_data()
