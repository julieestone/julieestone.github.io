from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Person

def homepage(request):
    person = Person.objects.first()
    return render(request, 'website/homepage.html', {'person': person})

def pups_and_quotes(request):
    return render(request, 'website/puppy_and_quotes.html')