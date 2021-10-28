import csv
from defs.database import insertDataBase
from defs.database import consultUser
from defs.check import logCheck, checkTimeDif, calcTime

# Lista que abrigará todos os dicionários referentes a cada linha de frequência registrada:
data = list()
error_log = list()
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
        row["total_hora"] = calcTime(final_time, initial_time)
        work_time = calcTime(final_time, initial_time)

        # Validação de log usando id (id_usuário), datas(inicio e fim) com a coleção de chaves válidas:
        if logCheck(id, initial_dat, final_dat, key_set, error_log):
            # Validação de datas comparando as entradas das datas de início e fim:
            if checkTimeDif(initial_time, final_time):
                # O retorno de confirmação (True) adiciona a linha(dicionário) na lista <data>:
                insertDataBase(id, initial_dat, initial_time, final_dat, final_time, work_time)
                data.append(row)
            else:
                # O retorno de negação (False) da função <checkTimeDif> ignora a linha:
                wrong_data.append(row)
        else:
            # O retorno de negação (False) da função <logCheck> ignora a linha:
            wrong_data.append(row)

print("\n------------------------------------------------Correct Data------------------------------------------------\n")

for i in data:
    print(i)

print("\n-------------------------------------------------Wrong Data-------------------------------------------------\n")

for i in wrong_data:
    print(i)

with open('lista_Invalida.csv', 'w', newline='') as listaInvalida:
    fieldnames = ["id_usuario", "data_inicio", "data_fim", "hora_inicio", "hora_fim", "total_hora"]
    writer = csv.DictWriter(listaInvalida, fieldnames=fieldnames)
    writer.writeheader()
    for row in wrong_data:
        writer.writerow(row)

print("\n------------------------------------------------------------------------------------------------------------\n")
option = True
while option:
    print('Para consultar horas trabalhadas por um determinado funcionário digite [ 1 ] ou qualquer outro número encerra o programa')
    choice = input('Informe sua escolha: ')
    if choice == '1':
        print("\n----------------------------------------Consultar horas trabalhadas-----------------------------------------\n")
        consultUser(input('Informe a matrícula para pesquisa: '))
        print("\n------------------------------------------------------------------------------------------------------------\n")
    else:
        option = False
        print('Programa encerrado.')
