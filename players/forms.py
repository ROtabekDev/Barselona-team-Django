from dataclasses import field
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Belgilanmagan"

    class Meta:
        model = Players
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("200 ta simvoldan uzun.")

        return title



class RegisterUserForm(UserCreationForm):

    username =  forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class': 'form-input'})),
    password1 = forms.CharField(label='Parol',widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    password2 = forms.CharField(label='Qayta parol',widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2') 

class LoginUserForm(AuthenticationForm): 
    username =  forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'})),
    password = forms.CharField(label='Parol',widget=forms.PasswordInput(attrs={'class': 'form-input'})),
    