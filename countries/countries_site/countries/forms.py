# countries/forms.py
from django import forms

class CountrySearchForm(forms.Form):
    query = forms.CharField(label='Search for a country', max_length=100)