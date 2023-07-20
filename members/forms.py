from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, User
from django import forms

class UserRegisterForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })

        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password Confirmation',
        })

    class Meta:
        model=User
        fields=('email','password1','password2')


class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=(
            'first_name',
            'last_name',
            'nick_name',
            # 'age',
            # 'email',
            'phone',
            'shirt_size',
            'retire_year',
            'bio',
            # 'player_type',
        )
        labels={
            'first_name':'First name',
            'last_name':'Last name',
            'nick_name':'Nickname on the court',
            # 'age':'Age',
            # 'email':'Email',
            'phone':'Phone',
            'shirt_size':'Shirt size',
            'retire_year':'Retire year (select the year you retire from team or leave the birmingham)',
            'bio':'bio',
            'player_type':'Player type ',
        }


        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            'nick_name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            # 'age':forms.TextInput(attrs={'class':'form-control','placeholder':'age'}),
            # 'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'shirt_size':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'retire_year':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'bio':forms.Textarea(attrs={'class':'form-control','placeholder':'introduce yourself here'}),
            # 'player_type':forms.Select()
        }

