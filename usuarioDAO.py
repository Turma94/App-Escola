import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor=conn.cursor()
    return conn, cursor


def criarTabelaUsuario():
    #Terminar a tabela de Usuario para isso precisa terminar a de usuario
    conn, cursor = connect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USUARIO(
     idUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome text not null,
     sobrenome text not null,
     senha text not null,
     email text not null,
     nivel TEXT CHECK( nivel IN ('COMUM','ADM','SUPER') )   NOT NULL DEFAULT 'COMUM'
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def addUsuario(nome,sobrenome,senha,email,nivel):
    criarTabelaUsuario()
    conn, cursor = connect()
    cursor.execute("""
        INSERT INTO USUARIO (nome,sobrenome,senha,email,nivel)
        VALUES(?,?,?,?,?)
    """,(nome,sobrenome,senha,email,nivel))
    conn.commit()
    cursor.close()
    conn.close()
    print("Cadastrado com sucesso!")


def listarUsuario():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM USUARIO
    """)
    conn.commit()
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

    # addUsuario("Maria","Rocha",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "maria@gmail.com","COMUM")
    #
    # addUsuario("IAN","Silva",
    #            "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
    #            "ian@gmail.com","COMUM")

    for i in listarUsuario():
        print(i)