import csv

with open('../venv/Teste.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:

        initialHour = row[2].replace(":", "")

        if row[2].isnumeric() is False and row[2] == 'Hora inicio':
            print(row[2])

        elif initialHour.isnumeric() is True and len(initialHour) == 6:
            print(initialHour)

        else:
            print('Dado não está no formato de Hora!')

        line_count += 1

    print(f'Quantidade de linhas: {line_count}')
