from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country_list'),
]
