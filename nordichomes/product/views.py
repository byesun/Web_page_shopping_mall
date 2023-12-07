from django.shortcuts import render, get_object_or_404

from .models import Product

def product(request, slug):
    products = Product.objects.filter(slug=slug)

    product = products.first()

    return render(request, 'product/product.html', {'product': product})