import csv
from defs.gen import dictGen

data = list()

with open("frequencia.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        dictGen(row, data)

for i in data:
    print(i)
