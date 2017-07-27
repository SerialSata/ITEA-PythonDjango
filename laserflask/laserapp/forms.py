from .models import Laserapp
from django import forms


class LaserappForm(forms.ModelForm):
    class Meta:
        model = Laserapp
        fields = '__all__'
