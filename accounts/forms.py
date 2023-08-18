from django import forms 
from .models import Student

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['avatar'] 