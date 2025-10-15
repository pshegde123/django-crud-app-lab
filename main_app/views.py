# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import RentalRecordForm

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
    rentalrecord_form = RentalRecordForm()
    return render(request, 'cars/details.html', {'car': car,'rentalrecord_form': rentalrecord_form})

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

def add_rentalrecord(request, car_id):
    # create a ModelForm instance using the data in request.POST
    form = RentalRecordForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_record = form.save(commit=False)
        new_record.car_id = car_id
        new_record.save()
    return redirect('car-detail', car_id=car_id)