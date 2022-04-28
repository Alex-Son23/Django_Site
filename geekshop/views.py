from django.shortcuts import render
# from ..mainapp.models import Product
from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        # basket_price = basket.price()

    content = {
        'title': 'главная',
        'products': products,
        'basket': basket
    }

    context = render(request, 'geekshop/index.html', context=content)
    return context


def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'контакты',
        'basket': basket
    }
    return render(request, 'geekshop/contact.html', context)

