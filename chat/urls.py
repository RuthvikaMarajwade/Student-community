from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.index, name='home1'),
    path('chat/<str:room_name>/', views.room, name='room'),
]