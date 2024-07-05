from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search/<str:source>/', views.search, name='search'),
    path('hotel',views.hotel,name='hotel'),
    path('flight',views.flight1,name='flight'),
    path('destination_list/<str:city_name>', views.destination_list, name='destination_list'),
    path('destination_list/destination_details/<str:city_name>', views.destination_details, name='destination_details'),
    path('destination_details/<str:city_name>', views.destination_details, name='destination_details'),
    path('customize',views.customize,name='customize'),
    path('checkout/hotel', views.checkout, name='checkout_hotel'),
    path('checkout/package', views.checkout, name='checkout_package'),
    path('checkout/flight', views.checkout, name='checkout_flight'),
    path('success',views.success,name='success'),
    path('trips',views.trips,name='trips')
]
