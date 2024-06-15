from django.db import models

# Create your models here.
class Inventory(models.Model):
    product_name=models.CharField(max_length=30,null=False,blank=False)
    cost_per_item=models.DecimalField(max_digits=12,decimal_places=2,null=False,blank=False)
    quantity_in_stock=models.IntegerField(null=False,blank=False)
    quantity_sold=models.IntegerField(null=False,blank=False)
    sales=models.DecimalField(max_digits=12,decimal_places=2,null=False,blank=False)
    stock_date=models.DateField()
    photos=models.ImageField(upload_to="Inventph/")

    def __str__(self):
        return self.product_name

class Weather(models.Model):
    formatted_date = models.DateTimeField()
    summary = models.CharField(max_length=200)
    precip_type = models.CharField(max_length=50, null=True, blank=True)
    temperature_c = models.FloatField()
    apparent_temperature_c = models.FloatField()
    humidity = models.FloatField()
    wind_speed_kmh = models.FloatField()
    wind_bearing_degrees = models.IntegerField()
    visibility_km = models.FloatField()
    loud_cover = models.FloatField()
    pressure_millibars = models.FloatField()
    daily_summary = models.TextField()

    def __str__(self):
        return self.precip_type
    
from django.db import models

class Movie(models.Model):
    poster_link = models.URLField()
    series_title = models.CharField(max_length=255)
    released_year = models.CharField(max_length=10)
    certificate = models.CharField(max_length=10)
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=255)
    imdb_rating = models.FloatField()
    overview = models.TextField()
    meta_score = models.CharField(max_length=10, null=True)
    director = models.CharField(max_length=255)
    star1 = models.CharField(max_length=255)
    star2 = models.CharField(max_length=255)
    star3 = models.CharField(max_length=255)
    star4 = models.CharField(max_length=255)
    no_of_votes = models.IntegerField()
    gross = models.CharField(max_length=255)  # Gross is a string due to commas and other characters

    def __str__(self):
        return self.series_title
    
class BusinessData(models.Model):
    series_reference = models.CharField(max_length=100)
    period = models.CharField(max_length=10)
    data_value = models.CharField(max_length=20,null=True, blank=True)
    suppressed = models.CharField(max_length=1, blank=True)  # Assuming suppressed is a single character
    status = models.CharField(max_length=1)
    units = models.CharField(max_length=20)
    magnitude = models.IntegerField()
    subject = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    series_title_1 = models.CharField(max_length=100)
    series_title_2 = models.CharField(max_length=100)
    series_title_3 = models.CharField(max_length=100)
    series_title_4 = models.CharField(max_length=100, blank=True)  # Depending on your data completeness
    series_title_5 = models.CharField(max_length=100, blank=True)  # Depending on your data completeness
    
    def __str__(self):
        return f"{self.series_reference} - {self.period}"
    
class Customer(models.Model):
    index = models.IntegerField(unique=True)
    customer_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone_1 = models.CharField(max_length=20, null=True, blank=True)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    subscription_date = models.DateField()
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.index}: {self.first_name} {self.last_name} ({self.customer_id})"

class Electronic(models.Model):
    series_reference = models.CharField(max_length=100)
    period = models.CharField(max_length=10)
    data_value = models.CharField(max_length=20,null=True, blank=True)
    suppressed = models.CharField(max_length=1, blank=True)  # Assuming suppressed is a single character
    status = models.CharField(max_length=1)
    units = models.CharField(max_length=20)
    magnitude = models.IntegerField()
    subject = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    series_title_1 = models.CharField(max_length=100)
    series_title_2 = models.CharField(max_length=100, blank=True, null=True)
    series_title_3 = models.CharField(max_length=100, blank=True, null=True)
    series_title_4 = models.CharField(max_length=100, blank=True, null=True)
    series_title_5 = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.series_reference} - {self.period}"
    

class Organization(models.Model):
    index = models.IntegerField(unique=True)
    organization_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    website = models.URLField()
    country = models.CharField(max_length=100)
    description = models.TextField()
    founded = models.IntegerField()
    industry = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()

    def __str__(self):
        return f"{self.index}: {self.name} ({self.organization_id})"

class People(models.Model):
    index = models.IntegerField(unique=True)
    user_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.index}: {self.first_name} {self.last_name} ({self.user_id})"

    
class QueryHistory(models.Model):
    user_id = models.IntegerField()
    query_history = models.JSONField()


    def __str__(self):
        return self.user_id
    
    