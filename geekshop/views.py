from django.shortcuts import render
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]

    content = {
        'title': 'главная',
        'products': products,
    }

    context = render(request, 'geekshop/index.html', context=content)
    return context


def contacts(request):

    context = {
        'title': 'контакты',
    }
    return render(request, 'geekshop/contact.html', context)

