from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postCar', views.postCar, name='postCar'),
    path('displayCars', views.displayCars, name='displayCars'),
    path('car_detail/<int:car_id>', views.car_detail, name='car_detail'),
    path('home', views.home, name='home'),
    path('myCars', views.myCars, name='myCars'),
    path('carDelete/<int:car_id>', views.carDelete, name='carDelete'),
    path('search', views.search, name='search'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
]

