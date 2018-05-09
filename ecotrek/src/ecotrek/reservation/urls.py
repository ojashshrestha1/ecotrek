from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('a/',  views.index, name='index'),
    path('add/',  views.add, name='add'),
    url(r'^details/(?P<id>\w{0,50})/$',  views.details)
   

    
]
# url(r'^details/(?P<id>\w{0,50})/$', views.details),



