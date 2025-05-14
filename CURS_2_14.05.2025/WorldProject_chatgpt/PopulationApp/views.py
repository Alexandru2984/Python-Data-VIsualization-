from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib

matplotlib.use("svg")

def all_countries_view(request):
    context = {}
    return render(request, 'all_countries.html', context)

def create_image(countries=["China", "India", "Brazil"], population=[1411, 1378, 213]):
    fig, axes = plt.subplots()
    axes.pie(population, labels=countries)
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode("utf-8")

suprafete = {
    'Bangladesh': 147570,
    'Brazil': 8515770,
    'China': 9562910,
    'India': 3287263,
    'Indonesia': 1904569,
    'Mexico': 1972550,
    'Nigeria': 923768,
    'Pakistan': 881913,
    'Russia': 17098242,
    'United States': 9831510
}

populatii = {
    'Bangladesh': 170,
    'Brazil': 213,
    'China': 1411,
    'India': 1378,
    'Indonesia': 271,
    'Mexico': 126,
    'Nigeria': 211,
    'Pakistan': 225,
    'Russia': 146,
    'United States': 331
}

def choose_countries_view(request):
    countries = list(populatii.keys())
    base64_image = None
    tari = []
    measure = "populatii"
    measured_data = populatii

    if request.method == "POST":
        measure = request.POST.get("measure", "populatii")
        tari = request.POST.getlist("countries")
        tari = [t for t in tari if t in countries]

        if measure == "suprafete":
            measured_data = suprafete
        else:
            measured_data = populatii

        if tari:
            locuitori = [measured_data[t] for t in tari]
            base64_image = create_image(tari, locuitori)

    context = {
        "countries": countries,
        "base64_image": base64_image,
        "tari": tari,
        "measure": measure,
    }
    return render(request, 'choose_countries.html', context)