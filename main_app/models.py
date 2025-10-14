from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    companyName = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    # new code below
    def __str__(self):
        return self.companyName
    
    # Define a method to get the URL for this particular car instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this car's details
        return reverse('car-detail', kwargs={'car_id': self.id})        