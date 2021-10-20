with open("frequencia.csv", "r", encoding='utf-8') as file:
    header = file.readline().rstrip()
    print(header.split('\t'))
    for row in file.readlines():
        line = row.rstrip()
        print(line.split('\t'))
