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


def addUsuario(nome, sobrenome, senha, email, nivel, status):
    conn, cursor = conected()
    cursor.execute("""
        INSERT INTO usuarios (nome,sobreNome,senha,email,nivel, status)
        VALUES(%s,%s,%s,%s,%s,%s);
    """, (nome, sobrenome, senha, email, nivel, status))
    conn.commit()
    cursor.close()
    conn.close()
    print("Cadastrado com sucesso!")


def deletarUsuario(email):
    conn, cursor = conected()
    try:
        cursor.execute("DELETE FROM usuarios WHERE email LIKE %s", (email,))
        conn.commit()
        print("Usuário e registros relacionados excluídos com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao deletar usuário:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


def selecionarUsuarioEmail(email):
    conn, cursor = conected()
    try:
        cursor.execute("""SELECT nome, sobreNome, email FROM usuarios WHERE email = %s""", (email,))
        lista = cursor.fetchall()
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar usuario:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


def listarUsuario():
    conn, cursor = conected()
    cursor.execute("""
    SELECT * FROM usuarios
    """)
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


def atualizarUsuario(nome, sobreNome, email, status, email_antigo):
    conn, cursor = conected()
    try:
        conn, cursor = conected()
        cursor.execute("UPDATE usuarios SET nome = %s, sobreNome = %s, email = %s, status = %s WHERE id IN (SELECT id "
                       "FROM (SELECT id FROM usuarios WHERE email = %s) AS subquery)",
                       (nome, sobreNome, email, status, email_antigo))
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
    # addUsuario("Carlos","Silva",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "sobralcomix@gmail.com","COMUM")
    #
    #
    addUsuario("Maria",
               "Rocha",
               "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
               "maria@gmail.com",
               "ADMINISTRADOR",
               True)
    #
    # addUsuario("IAN","Silva","03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4","ian@gmail.com","COMUM")

    # senhaGerada=criptografarSenha(input("digite uma senha: "))
    #
    # addUsuario("maria","rocha",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "maria@gmail.com","ADM")

    # for i in listarUsuario():
    #     print(i)
    #
    # print(selecionarUsuarioEmail('maria@gmail.com'))
    #
    # atualizarUsuario('nicolas', 'gama', 'nicollas@gmail.com', True, 'maria@gmail.com')
