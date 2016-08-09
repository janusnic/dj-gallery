from django.conf.urls import url
from .views import index
urlpatterns = [
    url(r'^$', index, name='index'),

    #url(r'^category/(?P<categoryslug>.*)/$', category, name='category'),
    #url(r'^categories/$', categories, name='categories'),
    #url(r"^archive/(\d+)/(\d+)/$", monthly_archive , name='archive'),
    #url(r'^(?P<postslug>.*)/$', detail, name='detail' ),
    #url(r'^(?P<post_id>[0-9]+)/$', detail, name='detail'),

]
