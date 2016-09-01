from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .fields import ThumbnailImageField
from PIL import Image as PImage

class Album(models.Model):
    """
    model for user albums
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    description = models.CharField(max_length=1024, verbose_name=_('Description'))
    category = models.ForeignKey("Category",null=False,blank=False)

    # preview/thumbnail image for an album
    cover = models.ImageField(upload_to = 'photos/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def photos(self):
        lst = [x.photo.name for x in self.photo_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')

    def delete(self, *args, **kwargs):
        for img in self.photo_set.all():
            img.delete()
        super(Album, self).delete(*args, **kwargs)

    def __str__(self):
        """
        function returns unicode representation of album
        """
        return "%s" % self.title

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

class Photo(models.Model):
    """
    model for user photos
    """
    user = models.ForeignKey(User)
    album = models.ForeignKey(Album)

    photo = ThumbnailImageField(upload_to='photos/', sizes=((40,40),(128,128)))
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    caption = models.CharField(max_length=250, blank=True, verbose_name=_('Caption'))
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Photo, self).save(*args, **kwargs)
        img = PImage.open(os.path.join(MEDIA_ROOT, self.photo.name))
        self.width, self.height = img.size
        super(Photo, self).save(*args, ** kwargs)

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super(Photo, self).delete(*args, **kwargs)

    def __str__(self):
        """
        function returns unicode representation of photo
        """
        return "%s" % self.img
