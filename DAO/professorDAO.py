import mysql.connector


def conected():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def addProfessor(categoria, email):
    conn, cursor = conected()
    try:
        cursor.execute("""INSERT INTO professor (categoria, idUsuario) SELECT %s, id FROM usuarios WHERE email = %s """,(categoria, email))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao deletar usuário:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def selectProfessor():
    conn, cursor = conected()
    cursor.execute("""
       SELECT * FROM professor
       """)
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

def atualizarProfessor(categoria, email):
    conn, cursor = conected()
    try:
        conn, cursor = conected()
        cursor.execute("UPDATE professor SET categoria = %s WHERE idUsuario IN (SELECT id FROM "
                       "usuarios WHERE email = %s)",
                       (categoria, email))
        conn.commit()
        print("Usuario e registros relacionados atualizada com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao atualizar usuario:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()



if __name__ == '__main__':
    pass

#
# addProfessor('ESTAGIO', 'nicollas@gmail.com')
atualizarProfessor('EFETIVO','nicollas@gmail.com')
