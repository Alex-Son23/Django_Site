import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


# def products(request, pk=None, page=1):
#     title = 'Каталог'
#     links_menu = ProductCategory.objects.filter(is_active=True)
#     products = Product.objects.all().order_by('price')
#
#     basket = get_basket(request.user)
#
#     if pk is not None:
#         if pk == 0:
#             category = {
#                 # 'pk': 0,
#                 'name': 'все',
#             }
#             products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
#
#         paginator = Paginator(products, 2)
#         try:
#             products_paginator = paginator.page(page)
#         except PageNotAnInteger:
#             products_paginator = paginator.page(1)
#         except EmptyPage:
#             products_paginator = paginator.page(paginator.num_pages)
#
#         context = {
#             'title': title,
#             'links_menu': links_menu,
#             'category': category,
#             'products': products_paginator,
#             'basket': basket
#         }
#
#         return render(request, 'mainapp/products_list.html', context=context)
#
#     hot_product = get_hot_product()
#     same_products = get_same_products(hot_product)
#
#     context = {
#         'title': title,
#         'links_menu': links_menu,
#         'products': products,
#         'hot_product': hot_product,
#         'same_products': same_products,
#         'basket': basket
#     }
#
#     return render(request, 'mainapp/products_list.html', context=context)
# return render(request, 'mainapp/products.html', context=context)


def products(request, pk=None, page=1):
    title = "Каталог"
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
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', context)

    hot_product = get_hot_product()
    same_product = get_same_products(hot_product)

    paginator = Paginator(products, 4)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    try:
        print(same_product[0])
        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_paginator,
            'hot_product': hot_product,
            'same_products': same_product,
            'basket': basket,
        }
    except IndexError:
        context = {
            'title': title,
            'links_menu': links_menu,
            'products': products_paginator,
            'hot_product': hot_product,
            'basket': basket,
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
