from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': 'User Name',
                'class': 'form-control'
            })
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Email',
                'class': 'form-control'
            })
        self.fields['password'].widget.attrs\
            .update({
                'placeholder': 'User Passord',
                'class': 'form-control'
            })

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
