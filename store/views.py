from django.shortcuts import render
from .models import User, Seller, Product, PaymentMethod, Order, Category, OrderDetail
from django.contrib.auth.models import User as dbUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def checkUser(request):
    user = request.user
    if user.is_authenticated:
        return user, True
    else:
        user.name = 'Anonymous'
        return user, False

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    user, logged = checkUser(request)
    return render(request, 'store/index.html', {
        'categories': categories,
        'products': products,
        'user': user,
        'logged': logged
    })

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    user, logged = checkUser(request)
    return render(request, 'store/product.html', {
        'product': product,
        'user': user,
        'logged': logged
    })

def category(request, category_id):
    user, logged = checkUser(request)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category_id).all()
    for product in products:
        fname = str(product.photo)
        fname = fname.split('/')
        name = fname[-1]
        product.photo = 'img/'+name
    return render(request, 'store/products.html', {
        'products': products,
        'categories': categories,
        'user': user,
        'logged': logged
    })

def signin(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request, user)
        user, logged = checkUser(request)
        message = "Sign in successful!"
        return render(request, 'store/index.html', {
            'msg': message,
            'user': user,
            'logged': logged})
    else:
        message = "Sign in unsuccesful, try again!"
        return render(request, 'store/signin.html', {
            'msg': message,
            'user': user,
            'logged': logged})

def signout(request):
    logout(request)
    message = "Sign out succesful!"
    user, logged = checkUser(request)
    return render(request, 'store/index.html', {
        'msg': message,
        'user': user,
        'logged': logged})

def register(request):
    user = User()
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.password = request.POST['password']
    toUser = dbUser.objects.create_user(username=user.email, password=user.password)
    user.save()
    message = "Sign up Successful!"
    return render(request, 'store/index.html', {
        'msg' : message})

def toSignin(request):
    return render(request, 'store/signin.html', {})

def toRegister(request):
    return render(request, 'store/register.html', {})

def desc(request):
    desc = Product.objects.all()
    return render(request, 'store/product_desc.html', {'desc':desc})

# def slider(request):
#     return render(request, 'store/slider-banner.html', {})

# def header(request):
#     return render(request, 'store/header.html', {})

# def cart0(request):
#     return render(request, 'store/cart0.html', {})

# def cart1(request):
#     return render(request, 'store/cart1.html', {})

# def footer(request):
#     return render(request, 'store/footer.html', {})

# def search(request):
#     return render(request, 'store/search.html', {})
