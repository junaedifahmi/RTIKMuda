from django.conf.urls import url

from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^tambah/$', Tambah.as_view(), name='tambah'),
    url(r'^(?P<pk>[0-9]+)/$', Detail.as_view(), name='detail'),
]