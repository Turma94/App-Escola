import sqlite3 as sq

def connect():
    conn=sq.connect(r"../bancoTeste.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor=conn.cursor()
    return conn, cursor

def criarTabelaMateria():
    conn, cursor = connect()
    cursor.execute("""CREATE TABLE IF NOT EXISTS MATERIA(
     idMateria INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     nome text not null
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def addMateria(nome_materia):
    criarTabelaMateria()
    conn, cursor = connect()
    cursor.execute("""
    INSERT INTO MATERIA(nome) values(?);
    """,(nome_materia,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add com sucesso! ")


def listarMaterias():
    conn, cursor = connect()
    cursor.execute("""
    SELECT * FROM MATERIA;
    """)
    conn.commit()
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista


if __name__ == '__main__':
    # addMateria("Matematica")
    # addMateria("Português")
    # addMateria("Geografia")
    # addMateria("Física")
    for materia in listarMaterias():
        print(materia)