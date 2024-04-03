import mysql.connector


def conected():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def addProfessor(nome, sobrenome, categoria):
    conn, cursor = conected()
    try:
        cursor.execute("""INSERT INTO professor (categoria, idUsuario) SELECT %s, id FROM usuarios WHERE nome = %s AND sobreNome = %s""",
                       (categoria, nome, sobrenome))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar professor:", error)
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
        print("Professor e registros relacionados atualizada com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao atualizar professor:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


def selecionarEmailProfessor(emailUsuario):
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT usuarios.nome, usuarios.email, professor.categoria FROM usuarios JOIN professor ON 
        usuarios.id = professor.idUsuario WHERE usuarios.email = %s""",
                       (emailUsuario,))
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar professor:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def selecionarProfessor_porID(id):
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT usuarios.nome, usuarios.sobreNome  
        FROM usuarios 
        JOIN professor ON usuarios.id = professor.idUsuario 
        WHERE usuarios.id = %s""",
                       (id,))
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar professor:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def selecionarProfessor():
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT professor.id, usuarios.nome, usuarios.sobreNome, professor.categoria
        FROM usuarios 
        JOIN professor  ON usuarios.id = professor.idUsuario""",
                       )
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar professor:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def selecionarIdProfessor(nome, sobrenome):
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT usuarios.id FROM usuarios JOIN professor ON 
        usuarios.id = professor.idUsuario WHERE usuarios.nome = %s AND usuarios.sobreNome = %s""",
                       (nome, sobrenome))
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar professor:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()



if __name__ == '__main__':


#
# addProfessor('ESTAGIO', 'nicollas@gmail.com')
# atualizarProfessor('ESTAGIO', 'nicollas@gmail.com')
# print(selecionarProfessor('VANESSA@contato.com'))
# atualizarProfessor('EVENTUAL','VANESSA@contato.com')
# addProfessor('Maria', 'Rocha', 'EFETIVO')

# print(selecionarIdProfessor('nicolas','gama'))
    print(selecionarProfessor_porID(1))