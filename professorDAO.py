import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor=conn.cursor()
    return conn, cursor


def criarTabelaProfessor():
    #Terminar a tabela de professor para isso precisa terminar a de usuario
    conn, cursor = connect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESSOR(
     idProfesor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     categoria TEXT CHECK( categoria IN ('EFETIVO','EVENTUAL','ESTAGIO') )   NOT NULL DEFAULT 'EFETIVO',
     id_usuario INTEGER  UNIQUE,
     FOREIGN KEY (id_usuario) REFERENCES USUARIO (idUsuario)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def addProfessor(categoria,id_usuario:int):
    criarTabelaProfessor()
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO PROFESSOR(categoria,id_usuario)
    VALUES(?,?)
    """,(categoria,id_usuario))
    conn.commit()
    cursor.close()
    conn.close()
    print("Adicionado com sucesso !")


def listarProfessores():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM PROFESSOR;
    """)
    conn.commit()
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    # addProfessor("EFETIVO",1)
    # addProfessor("EFETIVO",2)
    # addProfessor("EVENTUAL", 3)

    for prof in listarProfessores():
        print(prof)
