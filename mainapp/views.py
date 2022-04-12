from django.shortcuts import render


def products(request):
    return render(request, 'mainapp/products.html')

# Create your views here.
