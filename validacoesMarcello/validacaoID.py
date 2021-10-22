import csv

with open('../venv/Teste.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:

        if row[0].isnumeric() is False and row[0] == 'ID':
            print(row[0])

        elif row[0].isnumeric() is False and row[0] != 'ID':
            print(f'Coluna não é ID!')

        elif row[0].isnumeric() is True:
            print(row[0])

        else:
            print('Dado não é numérico!')

        line_count += 1

    print(f'Quantidade de linhas: {line_count}')



