import csv
from django.core.management.base import BaseCommand, CommandError
from myapps.models import Electronic  # Replace with your actual model import path

class Command(BaseCommand):
    help = 'Import electronic card transactions data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('electronic-card.csv', type=str, help='electronic-card.csv')

    def handle(self, *args, **options):
        csv_file = options['electronic-card.csv']

        # Clear existing data (optional)
        Electronic.objects.all().delete()

        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create a new ElectronicCardTransaction object for each row in the CSV
                Electronic.objects.create(
                    series_reference=row['Series_reference'],
                    period=row['Period'],
                    data_value=row['Data_value'],
                    suppressed=row['Suppressed'],
                    status=row['STATUS'],
                    units=row['UNITS'],
                    magnitude=row['Magnitude'],
                    subject=row['Subject'],
                    group=row['Group'],
                    series_title_1=row['Series_title_1'],
                    series_title_2=row.get('Series_title_2', ''),
                    series_title_3=row.get('Series_title_3', ''),
                    series_title_4=row.get('Series_title_4', ''),
                    series_title_5=row.get('Series_title_5', '')
                )

        self.stdout.write(self.style.SUCCESS('Electronic card transactions data imported successfully'))
