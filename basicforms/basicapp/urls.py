from django.contrib import admin
from django.urls import path
from basicapp import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^empform/$', views.empform, name='empform'),
]
