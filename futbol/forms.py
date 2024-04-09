from django import forms
from .models import Teams

class TeamsForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['team', 'country', 'city', 'logo', 'points']
