import csv
from django.core.management.base import BaseCommand, CommandError
from myapps.models import BusinessData  # Replace with your actual model import path

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('business-data.csv', type=str, help='business-data.csv')

    def handle(self, *args, **options):
        csv_file = options['business-data.csv']
        
        # Clear existing data (optional)
        BusinessData.objects.all().delete()
        
        # Open and read the CSV file
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Create a new BusinessData object for each row in the CSV
                BusinessData.objects.create(
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
                    series_title_2=row['Series_title_2'],
                    series_title_3=row['Series_title_3'],
                    series_title_4=row['Series_title_4'],
                    series_title_5=row['Series_title_5']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))