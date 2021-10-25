import csv

from defs.gen import insertDataBase
from defs.gen import validation


data = list()

with open("frequencia.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        resultRegistration = validation(row)
        if resultRegistration != None:
            print('Verificar erros.')
            break
        else:
            insertDataBase(row)

for i in data:
    print(i)
