from defs.gen import dictGen


data = list()

with open("frequencia.csv", "r", encoding='utf-8') as file:
    header = file.readline().rstrip().split(',')
    for row in file.readlines():
        line = row.rstrip().split(',')
        dictGen(line, data)


for i in data:
    print(i)
