
from utils.criptografia import criptografarSenha
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


def addUsuario(nome,sobrenome,senha,email,nivel):
    conn, cursor = conected()
    cursor.execute("""
        INSERT INTO usuarios (nome,sobreNome,senha,email,nivel)
        VALUES(%s,%s,%s,%s,%s);
    """,(nome,sobrenome,senha,email,nivel))
    conn.commit()
    cursor.close()
    conn.close()
    print("Cadastrado com sucesso!")



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
    addUsuario("maria","rocha",
               "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
               "maria@gmail.com","ADM")

    for i in listarUsuario():
        print(i)


