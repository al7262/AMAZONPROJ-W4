from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:product_id>', views.product, name="product"),
    path('category/<int:category_id>', views.category, name="category"),
    path('header', views.header, name = 'header'),
]
