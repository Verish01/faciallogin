import csv
from django.core.management.base import BaseCommand, CommandError
from myapps.models import Organization  # Replace with your actual model import path

class Command(BaseCommand):
    help = 'Import organization data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('organizations-10000.csv', type=str, help='Path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['organizations-10000.csv']

        # Clear existing data (optional)
        Organization.objects.all().delete()

        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create a new Organization object for each row in the CSV
                Organization.objects.create(
                    index=row['Index'],
                    organization_id=row['Organization Id'],
                    name=row['Name'],
                    website=row['Website'],
                    country=row['Country'],
                    description=row['Description'],
                    founded=row['Founded'],
                    industry=row['Industry'],
                    number_of_employees=row['Number of employees']
                )

        self.stdout.write(self.style.SUCCESS('Organization data imported successfully'))
