from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password', 'email')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields=('portfolio_site','profile_pic')
        widgets={
            'portfolio_site':forms.TextInput(attrs={'class':'form-control'}),
            'profile_pic' : forms.TextInput(attrs={'class':'form-control'}),
        }
