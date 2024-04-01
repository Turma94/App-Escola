import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='escola'
    )
    cursor=conn.cursor()
    return conn, cursor



def addMateria(nome_materia):

    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO MATERIA(nome) values(%s);
    """,(nome_materia,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add com sucesso! ")


def listarMaterias():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM MATERIA;
    """)

    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    # addMateria("Matematica")
    # addMateria("Português")
    # addMateria("Geografia")
    # addMateria("Quimica")
    for materia in listarMaterias():
        print(materia)