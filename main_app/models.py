from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    companyName = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

    # new code below
    def __str__(self):
        return self.companyName
    
    # Define a method to get the URL for this particular car instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this car's details
        return reverse('car-detail', kwargs={'car_id': self.id})        


class RentalRecord(models.Model):
    date = models.DateField('Rental Date')
    person = models.CharField()

    # Create a car_id column for each rental record in the database
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.person} on {self.date}"   

    class Meta:
        ordering = ['-date']  # This line makes the newest feedings appear first