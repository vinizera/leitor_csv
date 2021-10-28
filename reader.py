import csv
import mysql.connector
from defs.database import insertDataBase
from defs.database import consultUser, insertDataBase
import json

from defs.check import logCheck, checkTimeDif, calcTime

data = list()
error_log = list()
wrong_data = list()

with open("frequencia.csv", "r", encoding='utf-8') as file:

    reader = csv.DictReader(file)
    key_set = set()

    for row in reader:
        id = row["id_usuario"]
        initial_dat = row["data_inicio"]
        final_dat = row["data_fim"]
        initial_time = row["hora_inicio"]
        final_time = row["hora_fim"]
        row["total_hora"] = calcTime(final_time, initial_time)
        work_time = calcTime(final_time, initial_time)

        if logCheck(id, initial_dat, final_dat, key_set, error_log):

            if checkTimeDif(initial_time, final_time):

                insertDataBase(id, initial_dat, initial_time, final_dat, final_time, work_time)
                data.append(row)
            else:
                wrong_data.append(row)
        else:

            wrong_data.append(row)

with open('lista_Invalida.csv', 'w', newline='') as listaInvalida:
    fieldnames = ["id_usuario", "data_inicio", "data_fim", "hora_inicio", "hora_fim", "total_hora"]
    writer = csv.DictWriter(listaInvalida, fieldnames=fieldnames)
    writer.writeheader()
    for row in wrong_data:
        writer.writerow(row)

for d in data:
    print(d)

