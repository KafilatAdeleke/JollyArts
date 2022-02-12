from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})