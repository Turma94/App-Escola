
import mysql.connector

def conected():

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )
    cursor=conn.cursor()
    return conn, cursor


def addUsuario(nome,sobrenome,senha,email,nivel, status):
    conn, cursor = conected()
    cursor.execute("""
        INSERT INTO usuarios (nome,sobreNome,senha,email,nivel, status)
        VALUES(%s,%s,%s,%s,%s,%s);
    """,(nome,sobrenome,senha,email,nivel,status))
    conn.commit()
    cursor.close()
    conn.close()
    print("Cadastrado com sucesso!")

def deletarUsuario(email):
    conn, cursor = conected()
    try:
        conn, cursor = conected()
        cursor.execute("DELETE FROM usuarios WHERE email LIKE %s", (email,))
        conn.commit()
        print("Usuário e registros relacionados excluídos com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao deletar usuário:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.commit()
            cursor.close()
            conn.close()


def listarUsuario():
    conn, cursor= conected()
    cursor.execute("""
    SELECT * FROM usuarios
    """)
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    pass
    # addUsuario("Carlos","Silva",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "sobralcomix@gmail.com","COMUM")
    #

    # addUsuario("Maria",
    #            "Rocha",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "maria@gmail.com",
    #            "COMUM")
    #
     #addUsuario("IAN","Silva","03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4","ian@gmail.com","COMUM")

    # senhaGerada=criptografarSenha(input("digite uma senha: "))
    #
    # addUsuario("maria","rocha",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "maria@gmail.com","ADM")

    for i in listarUsuario():
        print(i)

    deletarUsuario('amanda@contato.com')

