from django.urls import path

from . import views

app_name = 'userLog'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('driver_info/', views.driverInfo, name='driverInfo'),
    path('driver_info/status/', views.driverPage, name='driverPage'),
    path('rider/', views.riderPage, name='riderPage'),
    path('rideRequest/', views.rideRequest, name='rideRequest'),
    path('owner/', views.owner, name='owner')
]