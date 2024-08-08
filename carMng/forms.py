from django import forms
from django.forms import ModelForm
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = [
            'make',
            'model',
            'year',
            'mileage',
            'drivetrain',
            'engine',
            'transmission',
            'price',
            'description',
            'picture',
        ]