# main_app/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def index(request):
    # Send a simple HTML response
    return render(request, 'index.html')

def about(request):    
    return render(request, 'about.html')

def details(request):
    # Send a simple HTML response
    return render(request, 'details.html')

def car_index(request):
    cars = Car.objects.all()  
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/details.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
   
class CarUpdate(UpdateView):
    model = Car
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['model', 'description', 'year']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'