from django.urls import path
from rpi_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('led_control/', views.led_control, name='led_control'),
    path('video_feed/', views.video_feed, name='video_feed'),
]