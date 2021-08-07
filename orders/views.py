from django.http import response
from store.models import Product
from django.shortcuts import render
from django.http.response import JsonResponse

from sepet.basket import Sepet
from .models import Order, OrderItem

def add(request):
    sepet = Sepet(request)
    if request.POST.get('action') == 'post':

        user_id = request.user.id
        order_key = request.POST.get('order_key')
        sepettotal = sepet.get_total_price()

        if Order.objects.filter(order_key=order_key).exists():
            pass
        
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address='add',
                                        total_paid=sepettotal, order_key=order_key)

            order_id = order.pk
            for item in sepet:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], qt=item['qt'])
            response = JsonResponse({'success': 'tamamlandi'})
            return response