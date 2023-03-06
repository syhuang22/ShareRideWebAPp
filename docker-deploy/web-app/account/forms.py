from django import forms
from .models import DriverInfo, RideRequestInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DriverForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = ['fname','lname','carType','license','max_passenger']

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequestInfo
        fields = ['address','dateTime','carType','num_passenger','isShared','specialRequest']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')