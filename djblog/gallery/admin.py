from django.contrib import admin
from .models import Album, Photo, Category
# Register your models here.

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Category)
