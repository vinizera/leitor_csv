with open("frequencia.csv", "r", encoding='utf-8') as file:
    header = file.readline().rstrip()
    print(header.split(','))
    for row in file.readlines():
        line = row.rstrip().split(',')
        print(line)
