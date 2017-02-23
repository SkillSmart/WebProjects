from django import forms
from django.contrib.auth.models import User
from UserManagement.models import Attendent

class UserModelForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    passwordRepeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email', 'password', 'passwordRepeat']


class AttendentModelForm(forms.ModelForm):
    class Meta:
        model = Attendent
        fields = ['role']

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
