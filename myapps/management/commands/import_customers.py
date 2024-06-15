import csv
from django.core.management.base import BaseCommand, CommandError
from myapps.models import Customer  # Replace with your actual model import path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import customer data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('customers-10000.csv', type=str, help='customers-10000.csv')

    def handle(self, *args, **options):
        csv_file = options['customers-10000.csv']

        # Clear existing data (optional)
        Customer.objects.all().delete()

        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse the subscription date
                subscription_date = datetime.strptime(row['Subscription Date'], '%Y-%m-%d').date()

                # Create a new Customer object for each row in the CSV
                Customer.objects.create(
                    index=row['Index'],
                    customer_id=row['Customer Id'],
                    first_name=row['First Name'],
                    last_name=row['Last Name'],
                    company=row['Company'],
                    city=row['City'],
                    country=row['Country'],
                    phone_1=row['Phone 1'],
                    phone_2=row['Phone 2'],
                    email=row['Email'],
                    subscription_date=subscription_date,
                    website=row['Website']
                )

        self.stdout.write(self.style.SUCCESS('Customer data imported successfully'))
