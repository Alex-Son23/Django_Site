import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk).order_by('price')

    return same_products


def products(request, pk=None):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    products = Product.objects.all().order_by('price')

    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket
        }

        return render(request, 'mainapp/products_list.html', context=context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    title = 'детали продукта'
    links_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)

    basket = get_basket(request.user)

    same_products = get_same_products(product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': product,
        'same_products': same_products,
        'basket': basket
    }

    return render(request, 'mainapp/product.html', context=context)
# Create your views here.
