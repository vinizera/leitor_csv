import mysql.connector


def csvGen(data):
    return 0


def dictGen(data_row, data_list):
    data_dict = dict()
    data_dict['id_usuario'] = data_row[0]
    data_dict['data_inicio'] = data_row[1]
    data_dict['hora_inicio'] = data_row[2]
    data_dict['data_fim'] = data_row[3]
    data_dict['hora_fim'] = data_row[4]
    data_list.append(data_dict)

def insertDataBase(row):
    connection = mysql.connector.connect(host='localhost', database='work_time', user='root', password='1234')
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO informacoes (id_user, date_start, hour_start, date_end, hour_end)" \
                  "VALUES (%s, %s, %s, %s, %s)"
            values = (row[0], row[1], row[2], row[3], row[4])
            cursor.execute(sql, values)
            connection.commit()

    except ValueError:
        print('Erro para inserir no banco')

    finally:
        if connection.is_connected():
             cursor.close()
             connection.close()
             print('Conexão ao MySql encerrada.')

def validation(row):
    if len(row[0]) > 7 or row[0].isnumeric() is False:
        print(f'Verificar matrícula {row[0]}.')
    elif (len(row[1].split('-')[0]) != 4 or row[1].split('-')[0].isnumeric() is False) \
            or (len(row[1].split('-')[1]) != 2 or (int(row[1].split('-')[1]) < 0 or int(row[1].split('-')[1]) > 12) or row[1].split('-')[1].isnumeric() is False) \
            or (len(row[1].split('-')[2]) != 2 or (int(row[1].split('-')[2]) < 0 or int(row[1].split('-')[2]) > 31) or row[1].split('-')[2].isnumeric() is False):
        print(f'Data no formato inválido {row[1]} para matrícula {row[0]}.')
    elif (len(row[2].split(':')[0]) != 2 or (int(row[2].split(':')[0]) < 0 or int(row[2].split(':')[0]) > 23) or
          row[2].split(':')[0].isnumeric() is False) \
         or (len(row[2].split(':')[1]) != 2 or (int(row[2].split(':')[1]) < 0 or int(row[2].split(':')[1]) > 59) or
             row[2].split(':')[1].isnumeric() is False) \
         or (len(row[2].split(':')[2]) != 2 or (int(row[2].split(':')[2]) < 0 or int(row[2].split(':')[2]) > 59) or
             row[2].split(':')[2].isnumeric() is False):
        print(f'Hora no formato inválido {row[2]} para matrícula {row[0]}')
    elif (len(row[3].split('-')[0]) != 4 or row[3].split('-')[0].isnumeric() is False) \
            or (len(row[3].split('-')[1]) != 2 or (int(row[3].split('-')[1]) < 0 or int(row[3].split('-')[1]) > 12) or row[3].split('-')[1].isnumeric() is False) \
            or (len(row[3].split('-')[2]) != 2 or (int(row[3].split('-')[2]) < 0 or int(row[3].split('-')[2]) > 31) or row[3].split('-')[2].isnumeric() is False):
            print(f'Data no formato inválido {row[3]} para matrícula {row[0]}.')
    elif (len(row[4].split(':')[0]) != 2 or (int(row[4].split(':')[0]) < 0 or int(row[4].split(':')[0]) > 23) or
          row[2].split(':')[0].isnumeric() is False) \
            or (len(row[4].split(':')[1]) != 2 or (int(row[4].split(':')[1]) < 0 or int(row[4].split(':')[1]) > 59) or
                row[4].split(':')[1].isnumeric() is False) \
            or (len(row[4].split(':')[2]) != 2 or (int(row[4].split(':')[2]) < 0 or int(row[4].split(':')[2]) > 59) or
                row[2].split(':')[2].isnumeric() is False):
            print(f'Hora no formato inválido {row[4]} para matrícula {row[0]}')
