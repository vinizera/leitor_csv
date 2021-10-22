import csv

with open('../venv/Teste.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:

        finalDate = row[3].replace("/", "")

        if row[3].isnumeric() is False and row[3] == 'Data final':
            print(row[3])

        elif finalDate.isnumeric() is True and len(finalDate) == 8:
            print(finalDate)

        else:
            print('Dado não está no formato de Data!')

        line_count += 1

    print(f'Quantidade de linhas: {line_count}')

