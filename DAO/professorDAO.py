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
        cursor.execute("""INSERT INTO professor (categoria, idUsuario) SELECT %s, id FROM usuarios WHERE email = %s """,
                       (categoria, email))
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


def selecionarProfessor(emailUsuario):
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT usuarios.nome, usuarios.email, professor.categoria FROM usuarios JOIN professor ON 
        usuarios.id = professor.idUsuario WHERE usuarios.email = %s""",
                       (emailUsuario,))
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar usuario:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()



if __name__ == '__main__':
    pass

#
# addProfessor('ESTAGIO', 'nicollas@gmail.com')
# atualizarProfessor('ESTAGIO', 'nicollas@gmail.com')
print(selecionarProfessor('VANESSA@contato.com'))
atualizarProfessor('EVENTUAL','VANESSA@contato.com')