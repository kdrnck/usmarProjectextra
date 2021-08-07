from django.http import JsonResponse, response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from store.models import Product
from .basket import Sepet
from sepet import basket


def sepet_summary(request):
    sepet = Sepet(request)
    return render(request, 'sepet/summary.html', {'basket': sepet})

def sepet_add(request):
    sepet = Sepet(request)
    if request.POST.get('action') == 'post':
        print(request.POST.get.__dict__)
        product_id = int(request.POST.get('productid'))

        product_qt = int(request.POST.get('productqt'))
        product = get_object_or_404(Product, id=product_id)
        sepet.add(product=product, qt=product_qt)
        sepetqt = sepet.__len__()

        response = JsonResponse({'qt': sepetqt})
        return response


def sepet_delete(request):
    sepet = Sepet(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        sepet.delete(product=product_id)

        basketqty = sepet.__len__()
        baskettotal = sepet.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

def sepet_clear(request):
    sepet = Sepet(request)
    if request.POST.get('action') == 'post':
        #product_id =  request.POST.get('productid')
        product_id = list(request.session._session_cache["skey"].keys())
        #print(f'{request.session.model.__dict__}')
        #print(f'product id is {product_id}')
        sepet.clear(product=product_id)
        return HttpResponse('please work')

def sepet_update(request):
    sepet = Sepet(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qt = int(request.POST.get('productqt'))
        sepet.update(product=product_id, qt=product_qt)

        print(product_id)
        print(product_qt)

        response = JsonResponse({'Success': True})
        return response

