import csv
with open("european_cities.csv", "r") as f:
    data = list(csv.reader(f, delimiter=';'))

for d in data:
    print(d)
