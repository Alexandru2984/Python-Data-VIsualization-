

# Luati un produs si il puneti in database, sa includa nume, descriere, slug, pret si imagine

# Luati 10 produse si le puneti in database

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from Shop.models import Product, Category 
import requests
import json
import time
import random


class Command(BaseCommand):
    help = "Fetch categories from https://dummyjson.com/products/categories"

    def handle(self, *args, **options):

        BASE_URL = 'https://dummyjson.com/'
        URL_PRODUCTS = BASE_URL + 'products'
        LIMIT = 0
        SKIP = 50
        response = requests.get(URL_PRODUCTS, params={'limit':LIMIT, 'skip':SKIP})
        product_list = response.json()['products']
        for prod_dict in product_list:
            name = prod_dict['title']
            slug = name.lower().replace(" ", "-")
            description = prod_dict['description']
            price = prod_dict['price']


            if Product.objects.filter(name=name, slug=slug, description=description):
                print("Produsul deja exista in baza de date...!!!")
                continue


            image_url = prod_dict['thumbnail']
            image_response = requests.get(image_url)
            image_content = image_response.content
            category_name = prod_dict['category']
            category_object = Category.objects.filter(name=category_name.title()).first()
            product = Product.objects.create(name=name, slug=slug, description=description, price=price)
            if category_object:
                product.category = category_object

            
            product.image.save(name, ContentFile(image_content))
            product.save()
            time.sleep(random.randint(1,3))
        print("Programul a rulat complet")