from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from django import forms

class UserRegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=('username','password1','password2')


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=(
            'first_name',
            'last_name',
            'nick_name',
            'age',
            'email',
            'phone',
            'shirt_size',
            'bio',
            'player_type',
        )

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter your first name'}),
            'last_name':forms.TextInput(),
            'nick_name':forms.TextInput(),
            'age':forms.TextInput(),
            'email':forms.EmailInput(),
            'phone':forms.TextInput(),
            'shirt_size':forms.TextInput(),
            'bio':forms.Textarea(),
            'player_type':forms.Select()
        }

