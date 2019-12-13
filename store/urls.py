from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:product_id>', views.product, name="product"),
    path('category/<int:category_id>', views.category, name="category"),
    path('registered', views.register, name = 'registered'),
    path('signedin', views.signin, name = 'signedin'),
    path('register', views.toRegister, name='register'),
    path('signin', views.toSignin, name='signin'),
    path('desc', views.desc, name='desc'),
    path('signout', views.signout, name="signout")
    # path('cart0', views.cart0, name = 'cart0'),
    # path('cart1', views.cart1, name = 'cart1'),
    # path('search', views.search, name = 'search'),
]
