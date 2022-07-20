from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class MyUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { key: '' for key in fields }
    