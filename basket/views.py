from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .basket import Basket


def basket_summary(request):

    return render(request, 'store/basket/summary.html')
