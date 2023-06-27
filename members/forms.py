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
        labels={
            'first_name':'First name',
            'last_name':'Last name',
            'nick_name':'Nickname',
            'age':'Age',
            'email':'Email',
            'phone':'Phone',
            'shirt_size':'Shirt size',
            'bio':'bio',
            'player_type':'Player type ',
        }


        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            'nick_name':forms.TextInput(attrs={'class':'form-control','placeholder':'nickname you prefer to be called on court'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'age'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'phone'}),
            'shirt_size':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'bio':forms.Textarea(attrs={'class':'form-control','placeholder':'introduce yourself here'}),
            'player_type':forms.Select()
        }

