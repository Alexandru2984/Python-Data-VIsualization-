from django.shortcuts import render
import matplotlib.pyplot as plt 
from io import BytesIO
import base64
import matplotlib
import pandas as pd
import os
# Create your views here.

matplotlib.use("svg")


def load_country_data():
    # Calea absolută către CSV (ajustăm în funcție de poziția  locală)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "tari.csv")

    df = pd.read_csv(csv_path)
    countries = df["Country"].tolist()
    population = df["Population"].tolist()
    return countries, population
def all_countries_view(request):
	context = {}
	return render(request, 'all_countries.html', context)

def create_image(countries, population):
    fig, ax = plt.subplots()
    ax.pie(population, labels=countries, autopct='%1.1f%%')
    
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    image_base64 = base64.b64encode(image_png).decode("utf-8")
    return image_base64

	# tari = "China_India.png"
	# path = "PopulationApp/static/"
	# image_path = path + tari
	# plt.savefig(image_path)
	#return image_path

def choose_countries_view(request):
    countries, population = load_country_data()
    base64_image = None

    if request.method == "POST":
        selected_countries = request.POST.getlist("countries")
        selected_population = [population[countries.index(c)] for c in selected_countries]
        base64_image = create_image(selected_countries, selected_population)

    context = {
        'countries': countries,
        'base64_image': base64_image,
    }
    return render(request, 'choose_countries.html', context)


