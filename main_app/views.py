# main_app/views.py

from django.shortcuts import render

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def index(request):
    # Send a simple HTML response
    return render(request, 'index.html')

def details(request):
    # Send a simple HTML response
    return render(request, 'details.html')