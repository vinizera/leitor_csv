import mysql.connector


def insertDataBase(id, initial_dat, initial_time, final_dat, final_time):
    connection = mysql.connector.connect(host='localhost', database='work_time', user='root', password='1234')
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO informacoes (id_user, date_start, hour_start, date_end, hour_end)" \
                  "VALUES (%s, %s, %s, %s, %s)"
            values = (id, initial_dat, initial_time, final_dat, final_time)
            cursor.execute(sql, values)
            connection.commit()

    except Exception as exp:
        print(exp)

    finally:
        if connection.is_connected():
             cursor.close()
             connection.close()
             # print('Conexão ao MySql encerrada.')