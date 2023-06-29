from django import forms
from .models import movie1

class MovieForm(forms.ModelForm):
    class Meta:
        model=movie1
        fields=['name','desc','year','im']