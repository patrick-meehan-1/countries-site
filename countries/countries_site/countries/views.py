# countries/views.py
from django.shortcuts import render
from .models import Country
from .forms import CountrySearchForm

def country_list(request):
    # Initializing the search form
    form = CountrySearchForm(request.GET or None)
    
    # If the form is valid and the user submitted a search query
    if form.is_valid():
        query = form.cleaned_data['query']
        # Perform a case-insensitive search on the country names
        countries = Country.objects.filter(name__icontains=query)
    else:
        # If no search query, display all countries
        countries = Country.objects.all()
    
    return render(request, 'countries/country_list.html', {'form': form, 'countries': countries})
