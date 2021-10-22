import csv

with open('../venv/Teste.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:

        initialDate = row[1].replace("/", "")

        if row[1].isnumeric() is False and row[1] == 'Data inicio':
            print(row[1])

        elif initialDate.isnumeric() is True and len(initialDate) == 8:
            print(initialDate)

        else:
            print('Dado não está no formato de Data!')

        line_count += 1

    print(f'Quantidade de linhas: {line_count}')
