from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Country

# Register the Country model
admin.site.register(Country)