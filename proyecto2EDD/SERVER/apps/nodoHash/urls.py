from django.conf.urls import url,include
from . import index

urlpatterns = [
    url(r'^$', index),
]
