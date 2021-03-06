from django.conf.urls import url
from . import views as album_views

urlpatterns = [
    url(r'^$', album_views.home, name='home'),
    url(r'^add_album/$', album_views.add_album, name='add_album'),
    url(r'^save_album/$', album_views.save_album, name='save_album'),
    url(r'^show_album/(?P<pk>[0-9]+)/$', album_views.show_album),
]
