import csv
from defs.check import logCheck, checkTimeDif, calculateTimeDif

# Lista que abrigará todos os dicionários referentes a cada linha de frequência registrada:
data = list()
wrong_data = list()



# Abertura do arquivo csv para leitura (file):
with open("frequencia.csv", "r", encoding='utf-8') as file:
    # Leitor do arquivo como dicionário (chaves = colunas; valores = campos);
    # * a função csv.DictReader ignora a apresentação do cabeçalho e transforma seus itens em chaves automaticamente:
    reader = csv.DictReader(file)
    # Coleção de chaves válidas únicas geradas na função logCheck:
    key_set = set()
    # Início de laço para leitura das linhas csv:
    for row in reader:
        id = row["id_usuario"]
        initial_dat = row["data_inicio"]
        final_dat = row["data_fim"]
        initial_time = row["hora_inicio"]
        final_time = row["hora_fim"]
        work_bank = row["banco_horas"]
        # Validação de log usando id (id_usuário), datas(inicio e fim) com a coleção de chaves válidas:
        if logCheck(id, initial_dat, final_dat, key_set):
            # Validação de datas comparando as entradas das datas de início e fim:
            if checkTimeDif(initial_time, final_time):
                # O retorno de confirmação (True) adiciona a linha(dicionário) na lista <data>:
                data.append(row)
            else:
                # O retorno de negação (False) da função <checkTimeDif> ignora a linha:
                wrong_data.append(row)
        else:
            # O retorno de negação (False) da função <logCheck> ignora a linha:
            wrong_data.append(row)

print("\n----------------------------------------------Entradas Corretas----------------------------------------------")
for i in data:
    print(i)

print("\n----------------------------------------------Entradas Erradas----------------------------------------------")

for i in wrong_data:
    print(i)


