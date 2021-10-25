import csv

with open('../venv/Teste.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:

        finalHour = row[4].replace(":", "")

        if row[4].isnumeric() is False and row[4] == 'Hora final':
            print(row[4])

        elif finalHour.isnumeric() is True and len(finalHour) == 6:
            print(finalHour)

        else:
            print('Dado não está no formato de Hora!')

        line_count += 1

    print(f'Quantidade de linhas: {line_count}')
