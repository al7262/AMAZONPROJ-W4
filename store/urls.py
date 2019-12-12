from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('home', views.index),
    path('', views.slider),
    path('header', views.header, name = 'header'),
]
