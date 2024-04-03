import mysql.connector

def conected():

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123',
            database='escola'
        )
        cursor=conn.cursor()
        return conn, cursor
    except Exception as e:
        return False



