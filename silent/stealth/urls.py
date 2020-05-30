from django.urls import include,path,re_path
from django.conf.urls import url

from . import views

app_name = 'stealth'
urlpatterns = [
    path('', views.index, name='index'),
    re_path('^', views.index, name='index'),
]
