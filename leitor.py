with open("frequencia.csv", "r", encoding='utf-8') as freq:
    freq.readline()
    for line in freq:
        print(line.rstrip())
