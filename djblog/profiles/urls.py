from django.conf.urls import include, url
from profiles import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),

    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),

]
