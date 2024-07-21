from . import views
from django.urls import path
from django.http import HttpResponse



urlpatterns = [
    path('', views.home, name="home"),
    path('room_data/<str:pk>/', views.room, name="room"),
]
