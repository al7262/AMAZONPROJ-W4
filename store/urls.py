from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('slider', views.slider),
    path('footer', views.footer)
]
