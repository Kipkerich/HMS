from django import forms
from .models import Client, HealthPrograme, Enrollment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
        
class HealthProgrameForm(forms.ModelForm):
    class Meta:
        model = HealthPrograme
        fields = "__all__"
        
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['client', 'program']