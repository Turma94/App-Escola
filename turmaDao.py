import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    cursor=conn.cursor()
    return conn, cursor


def criarTabela():
     conn, cursor=connect()
     cursor.execute("""CREATE TABLE if not exists TURMA (
     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     ano_letivo integer not null,
     periodo text not null,
     serie text not null, 
     sigla_turma text not null
     );
    """)

     conn.commit()
     cursor.close()
     conn.close()



def inserirTurma(ano_letivo,periodo,serie,sigla_turma):
    criarTabela()
    conn, cursor = connect()
    cursor.execute("""INSERT INTO TURMA (ano_letivo,periodo,serie,sigla_turma)
    VALUES(?,?,?,?)
    """,(ano_letivo,periodo,serie,sigla_turma))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add com sucesso !")


def selectTurma():
    conn, cursor = connect()
    cursor.execute("""SELECT * FROM TURMA """)
    conn.commit()
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista



if __name__ == '__main__':
    # inserirTurma("2024","Tarde","4","A")
    # inserirTurma("2024", "Manhão", "8", "B")
    # inserirTurma("2024", "Tarde", "5", "C")
    # inserirTurma("2024", "Noite", "6", "D")
    for turma in  selectTurma():
       print(turma)