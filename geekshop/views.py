from django.shortcuts import render
# from ..mainapp.models import Product
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:5]

    content = {
        'title': 'главная',
        'products': products
    }

    context = render(request, 'geekshop/index.html', context=content)
    return context


def contacts(request):
    return render(request, 'geekshop/contact.html')

