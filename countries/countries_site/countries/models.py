from django.db import models
import uuid

# Create your models here.
class Country(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name  # Display the country's name in the admin and other contexts
    


# How I populated the database with countries
"""
Step 1: python manage.py shell

Step 2: 
from countries.models import Country

country_names = [
    'Andorra', 'Australia', 'Brazil', 'Belgium', 'Canada', 'China', 'France', 
    'Germany', 'India', 'Indonesia', 'Ireland', 'Italy', 'Japan', 'Kenya', 
    'Luxembourg', 'Mexico', 'New Zealand', 'Nigeria', 'Portugal', 'Russia', 
    'South Africa', 'South Korea', 'Spain', 'Sweden', 'Thailand', 'Ukraine', 
    'United Kingdom', 'United States of America', 'Vietnam', 'Zambia'
]
for name in country_names:
    Country.objects.create(name=name)
"""
