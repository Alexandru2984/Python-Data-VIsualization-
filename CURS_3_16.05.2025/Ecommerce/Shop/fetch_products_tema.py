

# Luati un produs si il puneti in database, sa includa nume, descriere, slug, pret si imagine

# Luati 10 produse si le puneti in database

from django.core.management.base import BaseCommand, CommandError
from Shop.models import Product 
import requests
import json


class Command(BaseCommand):
    help = "Fetch categories from https://dummyjson.com/products/categories"

    def handle(self, *args, **options):

        BASE_URL = 'https://dummyjson.com/'
        URL_PRODUCTS = BASE_URL + 'products'
        LIMIT = 1
        response = requests.get(URL_PRODUCTS, params={'limit':LIMIT})
        product_list = response.json()['products']
        for prod_dict in product_list:
            name = prod_dict['name']
            slug = name.lower().replace("", "_")
            description = prod_dict['description']
            price = prod_dict['price']

            Product.objects.create(name=name, slug=slug, description=description, price=price)
        print("Programul a rulat complet")