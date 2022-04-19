from django.shortcuts import render
from .models import Product


def product(request, pk):
    print(pk)
    return


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    context = {
        'title':'каталог',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context=context)

# Create your views here.
