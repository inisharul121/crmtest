from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    message = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'message']
