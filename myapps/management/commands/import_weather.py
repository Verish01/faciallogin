import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from myapps.models import Weather

class Command(BaseCommand):
    help = 'Imports weather data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('weatherHistory.csv', type=str, help='weatherHistory.csv')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['weatherHistory.csv']
        
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            weather_data = []
            for row in reader:
                weather_instance = Weather(
                    formatted_date=parse_datetime(row['Formatted Date']),
                    summary=row['Summary'],
                    precip_type=row.get('Precip Type'),
                    temperature_c=float(row['Temperature (C)']),
                    apparent_temperature_c=float(row['Apparent Temperature (C)']),
                    humidity=float(row['Humidity']),
                    wind_speed_kmh=float(row['Wind Speed (km/h)']),
                    wind_bearing_degrees=int(row['Wind Bearing (degrees)']),
                    visibility_km=float(row['Visibility (km)']),
                    loud_cover=float(row['Loud Cover']),  # Fixed typo here from 'Loud Cover'
                    pressure_millibars=float(row['Pressure (millibars)']),
                    daily_summary=row['Daily Summary']
                )
                weather_data.append(weather_instance)

            Weather.objects.bulk_create(weather_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV'))