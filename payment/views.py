from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sepet import basket

from sepet.basket import Sepet


@login_required
def BasketView(request):
    sepet = Sepet(request)
    total = str(sepet.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    return render(request, 'payment/home.html')
