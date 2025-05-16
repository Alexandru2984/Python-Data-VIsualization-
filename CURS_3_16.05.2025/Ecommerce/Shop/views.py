from django.shortcuts import render
from .models import Product
# Create your views here.

def all_products_view(request):
	products = Product.objects.all()
	context = {
		'products' : products,
	}
	return render(request, 'all_products.html', context)

def product_details_view(request):
	context = {}
	return render(request, 'product details.html', context)
