from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('home', views.index),
]
