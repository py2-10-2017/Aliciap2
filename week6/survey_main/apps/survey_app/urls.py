from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^result/$', views.result),
    url(r'^survey/process/$', views.process) 
    # when you get a url that matches this regex, run the process function in the views file
]