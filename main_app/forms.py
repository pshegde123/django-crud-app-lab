from django import forms
from .models import RentalRecord

class RentalRecordForm(forms.ModelForm):
    class Meta:
        model = RentalRecord
        fields = ['date', 'person']
        widgets = {
                    'date': forms.DateInput(
                        format=('%Y-%m-%d'),
                        attrs={
                            'placeholder': 'Select a date',
                            'type': 'date'
                        }
                    ),
                }