from django import forms 
from .models import Landmark

class LandmarkForm(forms.ModelForm):

    class Meta: 
        model = Landmark
        feilds = ('name', 'address', 'photo_url', 'type', 'description')