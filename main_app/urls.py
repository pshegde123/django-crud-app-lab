from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('details/', views.details, name='details'),
]