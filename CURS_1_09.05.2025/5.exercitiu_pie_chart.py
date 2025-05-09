import matplotlib.pyplot as plt
import csv

countries = []
population = []
with open("tari.csv") as freader:
    csv_reader = csv.DictReader(freader)
    print(csv_reader)

    for row in csv_reader:
        countries.append(row["country"])
        population.append(int(row["population"]))

print("Countries", countries)
print("Population", population)
plt.title("Populatia celor mai mari 10 tari")
plt.pie(population, labels=countries);
plt.savefig("10_tari.png")


