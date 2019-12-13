from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [

    path('', views.index, name="index"),
    path('product/<int:product_id>', views.product, name="product"),
    path('category/<int:category_id>', views.category, name="category"),

    path('home', views.index),
    path('', views.slider),

    path('header', views.header, name = 'header'),
    path('cart0', views.cart0, name = 'cart0'),
    path('cart1', views.cart1, name = 'cart1'),

    path('slider', views.slider),
    # path('footer', views.footer)

]
