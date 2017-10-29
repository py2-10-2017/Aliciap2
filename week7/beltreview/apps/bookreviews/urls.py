from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reviewshome$', views.index),
    url(r'^add$',views.add),
    url(r'^create$', views.create),
    url(r'^(?P<book_id>\d+)$', views.show),
    url(r'^(?P<book_id>\d+)/create$', views.create_additional)
]

