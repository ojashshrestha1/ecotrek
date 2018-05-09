from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('add-hotel/',  views.add_hotel, name='add-hotel'),    
    path('hotellist/', views.hotellist, name='hotellist'),
    path('reservation-request/', views.hotel_reservation_list, name='reservation-request'),
    url(r'^reservation-request/hotel-details/(?P<id>\w{0,50})/$',  views.hotel_reservation_details),
    url(r'^hoteldetails/(?P<id>\w{0,50})/$',  views.hoteldetails),
    url(r'^reservation/(?P<id>\w{0,50})/$',  views.hotel_reservation),
    url(r'^hoteldetails/(?P<id>\w{0,50})/edit/$',  views.edit_hotel),
    url(r'^hoteldetails/(?P<id>\w{0,50})/delete/$',  views.delete_hotel),

]