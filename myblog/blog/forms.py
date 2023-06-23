from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
 password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput())
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
  widgets = {'username':forms.TextInput(),
  'first_name':forms.TextInput(),
  'last_name':forms.TextInput(),
  'email':forms.EmailInput(),
  }

class LoginForm(AuthenticationForm):
 username = UsernameField(widget=forms.TextInput())
 password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput())
