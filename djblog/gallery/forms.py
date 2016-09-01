from .models import Album,Category,Photo
from django import forms

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        exclude = ['user']

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['width','height','user']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
