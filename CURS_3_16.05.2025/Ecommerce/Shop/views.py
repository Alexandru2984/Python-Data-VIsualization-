from django.shortcuts import render
from .models import Product, Category
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

def all_categories_view(request):
	categories = Category.object.all()
	context = {
		'categories': categories
	}
	return render(request, 'all_categories.html', context)
