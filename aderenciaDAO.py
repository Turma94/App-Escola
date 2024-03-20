import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor=conn.cursor()
    return conn, cursor


def criarAderencia():
    conn, cursor=connect()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS ADERENCIA(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_professor integer,
    id_materia integer,
    FOREIGN KEY (id_professor) REFERENCES PROFESSOR (idProfesor),
    FOREIGN KEY (id_materia) REFERENCES MATERIA (idMateria)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def addAderencia(id_professor,id_materia):
    criarAderencia()
    conn, cursor = connect()
    cursor.execute("""
           INSERT INTO ADERENCIA (id_professor,id_materia)
           VALUES(?,?)
           """,(id_professor,id_materia))
    conn.commit()
    cursor.close()
    conn.close()
    print("Adicionado com sucesso !")

def listarProf_Materia_descricao():
    conn, cursor = connect()
    cursor.execute("""
       SELECT PROFESSOR.id_usuario, USUARIO.nome, USUARIO.sobrenome, MATERIA.nome 
       FROM ADERENCIA
       INNER JOIN PROFESSOR
       ON PROFESSOR.idProfesor=ADERENCIA.id_professor
       INNER JOIN USUARIO
       ON PROFESSOR.id_usuario = USUARIO.idUsuario
       INNER JOIN MATERIA
       ON MATERIA.idMateria=ADERENCIA.id_materia
       
        """)
    conn.commit()
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


def busca_Prof_Materia_usando_ID(id):
    conn, cursor = connect()
    cursor.execute("""
       SELECT PROFESSOR.id_usuario, USUARIO.nome, USUARIO.sobrenome, MATERIA.nome 
       FROM ADERENCIA
       INNER JOIN PROFESSOR
       ON PROFESSOR.idProfesor=ADERENCIA.id_professor
       INNER JOIN USUARIO
       ON PROFESSOR.id_usuario = USUARIO.idUsuario
       INNER JOIN MATERIA
       ON MATERIA.idMateria=ADERENCIA.id_materia
       WHERE ADERENCIA.id_materia =(?)
        """, (id,))
    conn.commit()
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


def listarAderencias():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM ADERENCIA """)
    conn.commit()
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    # #prof 1
    # addAderencia(1,1)
    # addAderencia(1, 2)
    # addAderencia(1, 4)
    #
    # # prof 2
    # addAderencia(2, 3)
    # addAderencia(2, 2)
    #
    # # prof 3
    # addAderencia(3, 4)

    for aderencia in listarAderencias():
        print(aderencia)

    print("#" * 30)
    for aderenciaDesc in listarProf_Materia_descricao():
        print(aderenciaDesc)

    print("#"*30)
    for buscarAderencia in busca_Prof_Materia_usando_ID(1):
        print(buscarAderencia)