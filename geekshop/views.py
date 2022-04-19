from django.shortcuts import render


def index(request):
    list_prams = {'no': 'Oh no'}

    context = render(request, 'geekshop/index.html', context=list_prams )
    return context


def contacts(request):
    return render(request, 'geekshop/contact.html')

