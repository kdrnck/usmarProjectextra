from django.shortcuts import render, get_object_or_404

from .models import Category, Product, ProductManager

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def main(request):
    products = Product.objects.all()
    return render(request, 'store/main.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/urun.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def all(request):
    products = Product.objects.all()
    return render(request, 'store/all.html', {'products': products})
