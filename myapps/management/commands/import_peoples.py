import csv
from django.core.management.base import BaseCommand, CommandError
from myapps.models import People  # Replace with your actual model import path
from datetime import datetime

class Command(BaseCommand):
    help = 'Import user data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('people-10000.csv', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['people-10000.csv']

        # Clear existing data (optional)
        People.objects.all().delete()

        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse the date of birth
                date_of_birth = datetime.strptime(row['Date of birth'], '%Y-%m-%d').date()

                # Create a new User object for each row in the CSV
                People.objects.create(
                    index=row['Index'],
                    user_id=row['User Id'],
                    first_name=row['First Name'],
                    last_name=row['Last Name'],
                    sex=row['Sex'],
                    email=row['Email'],
                    phone=row['Phone'],
                    date_of_birth=date_of_birth,
                    job_title=row['Job Title']
                )

        self.stdout.write(self.style.SUCCESS('User data imported successfully'))
