import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def addMateria(nome_materia):
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO materia(nome) values(%s);
    """, (nome_materia,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add com sucesso! ")


def listarMaterias():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM materia;
    """)

    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


def atualizarMateria(nome, nome_antigo):
    conn, cursor = connect()
    try:
        cursor.execute("UPDATE materia SET nome = %s WHERE nome = %s", (nome, nome_antigo))
        conn.commit()
        print("Materia e registros relacionados atualizado com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao atualizar materia:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == '__main__':
    # addMateria("Matematica")
    # addMateria("Português")
    # addMateria("Geografia")
    # addMateria("Quimica")
    for materia in listarMaterias():
        print(materia)

atualizarMateria('Geografia', 'ingles')
