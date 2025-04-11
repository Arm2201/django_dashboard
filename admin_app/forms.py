from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())  # Use password1 as the login password field
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

