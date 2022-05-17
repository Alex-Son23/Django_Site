from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    context = {
        'title': title,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/list.html', context)


@login_required
def basket_add(request, pk):
    # print(request.META.get('HTTP_REFERER'), '\n', request.META)
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:detail', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    print(product)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    quantity = int(quantity)
    new_basket_item = Basket.objects.get(pk=int(pk))

    if quantity > 0:
        new_basket_item.quantity = quantity
        new_basket_item.save()
    else:
        new_basket_item.delete()

    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

    context = {
        'basket_items': basket_items,
    }

    result = render_to_string('basketapp/includes/inc_basket_list.html', context)

    return JsonResponse({'result': result})
