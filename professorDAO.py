import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    cursor=conn.cursor()
    return conn, cursor


def criarTabelaProfessor():
    #Terminar a tabela de professor para isso precisa terminar a de usuario
    conn, cursor = connect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESSOR(
     idProfesor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     categoria text not null
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()
