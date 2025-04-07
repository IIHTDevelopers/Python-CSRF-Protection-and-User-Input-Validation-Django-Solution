# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError

# Registration form with validation
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, required=True)
    
    def clean_username(self):
        """Validate that the username does not contain 'admin'"""
        username = self.cleaned_data['username']
        if 'admin' in username:
            raise ValidationError('Username cannot contain "admin"')
        return username

    def clean_email(self):
        """Validate that the email is not from 'spam.com'"""
        email = self.cleaned_data['email']
        if email.endswith('@spam.com'):
            raise ValidationError('Email from spam.com is not allowed')
        return email

# Registration view to process form submission
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the valid form (e.g., create user)
            return HttpResponse("Registration successful")
        else:
            return render(request, 'registration_form.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

# Home view (To be used in functional and boundary tests)
def home(request):
    return HttpResponse("Welcome to the home page!")
