import mysql.connector


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
             # print('Conexão ao MySql encerrada.')


def consultUser(id):
    connection = mysql.connector.connect(host='localhost', database='work_time', user='root', password='1234')
    try:
        cursor = connection.cursor()
        consult_sql = "SELECT * FROM informacoes WHERE id_user = %s"
        values = (id, )
        cursor.execute(consult_sql, values)
        rows = cursor.fetchall()

        if not rows:
            print('Matrícula não encontrada')
        else:
            for row in rows:
                print('Matrícula: ', row[1])
                print('Horas trabalhadas: ', row[6])

    except Exception as exp:
        print(exp)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print('Conexão ao MySql encerrada.')