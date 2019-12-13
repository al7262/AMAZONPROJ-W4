from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('home', views.index),
    path('', views.slider),
    path('header', views.header, name = 'header'),
    path('cart0', views.cart0, name = 'cart0'),
    path('cart1', views.cart1, name = 'cart1'),
    path('search', views.search, name = 'search'),
]
