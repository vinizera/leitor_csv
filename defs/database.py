import mysql.connector

# Insere informações no bando de dados MySql
def insertDataBase(id, initial_dat, initial_time, final_dat, final_time, work_time):
    connection = mysql.connector.connect(host='localhost', database='work_time', user='root', password='1234')
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO informacoes (id_user, date_start, hour_start, date_end, hour_end, worked_hours)" \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            values = (id, initial_dat, initial_time, final_dat, final_time, work_time)
            cursor.execute(sql, values)
            connection.commit()

    except Exception as exp:
        print(exp)

    finally:
        if connection.is_connected():
             cursor.close()
             connection.close()


# Consulta informações no bando de dados MySql
def consultUser(id):
    connection = mysql.connector.connect(host='localhost', database='work_time', user='root', password='1234')
    try:
        cursor = connection.cursor()
        cursor.execute("""SELECT time_format(SEC_TO_TIME(SUM(TIME_TO_SEC(worked_hours))),'%H:%i:%S')
        AS total_horas FROM informacoes where id_user = %s""", (id, ))
        rows = cursor.fetchall()
        if not rows[0][0]:
            print('Matrícula não encontrada')
        else:
            print(f'A matrícula \033[4;36m{id}\033[m tem como horas trabalhadas: \033[4;36m{rows[0][0]}\033[m')

    except Exception as exp:
        print(exp)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
