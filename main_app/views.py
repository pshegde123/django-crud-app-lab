# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car , RentalRecord
from .forms import RentalRecordForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

# Define the home view function
# def home(request):
#     # Send a simple HTML response
#     return render(request, 'home.html')
class Home(LoginView):
    template_name = 'home.html'

def index(request):
    # Send a simple HTML response
    return render(request, 'index.html')

def about(request):    
    return render(request, 'about.html')

def details(request):
    # Send a simple HTML response
    return render(request, 'details.html')

@login_required
def car_index(request):
    #cars = Car.objects.all()  
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    rentalrecord_form = RentalRecordForm()
    return render(request, 'cars/details.html', {'car': car,'rentalrecord_form': rentalrecord_form})

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    fields = '__all__'
    
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
   
class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car  
    fields = ['model', 'description', 'year']

class CarDelete(LoginRequiredMixin,DeleteView):
    model = Car
    success_url = '/cars/'

@login_required
def add_rentalrecord(request, car_id):
    # create a ModelForm instance using the data in request.POST
    form = RentalRecordForm(request.POST)
    # validate the form
    if form.is_valid():       
        new_record = form.save(commit=False)
        new_record.car_id = car_id
        new_record.save()
    return redirect('car-detail', car_id=car_id)

def show_updaterecord(request, car_id, record_id):        
    form = RentalRecordForm(request.POST)
    obj_to_update = RentalRecord.objects.get(id=record_id)       
    form.person = obj_to_update.person
    return render(request,'cars/record.html',{'form':form,'car_id':car_id ,'record_id':record_id})

#def update_rentalrecord(request, car_id, record_id):  
@login_required
def update_rentalrecord(request, car_id, record_id):  
    # model = RentalRecord          
    # return render(request,'cars/index.html')
    # form = RentalRecordForm(request.POST)
    # if form.is_valid():       
    #     new_record = form.save(commit=False)
    #     new_record.car_id = car_id
    #     new_record.save()
    obj_to_update = RentalRecord.objects.get(id=record_id)   
    form = RentalRecordForm(request.POST) 
    if form.is_valid():       
        date = form.cleaned_data['date']
        person = form.cleaned_data['person']
        obj_to_update.date = date
        obj_to_update.person = person
        obj_to_update.save()
    return redirect('car-detail', car_id=car_id)


def delete_rentalrecord(request, car_id, record_id):   
    obj_to_delete = RentalRecord.objects.get(id=record_id)       
    obj_to_delete.delete()
    return redirect('car-detail', car_id=car_id)