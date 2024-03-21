import sqlite3 as sq

def connect():
    conn=sq.connect(r"bancoTeste.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor=conn.cursor()
    return conn, cursor

def criarTabelaAula():
    conn, cursor=connect()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AULA(
    idAula INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_turma INTEGER NOT NULL,
    id_professor_responsavel INTEGER NOT NULL,
    id_professor_presente INTEGER NOT NULL,
    id_materia INTEGER NOT NULL,
    data VARCHAR(10),
    status BOOLEAN,
    FOREIGN KEY (id_turma) REFERENCES TURMA (id),
    FOREIGN KEY (id_professor_responsavel) REFERENCES PROFESSOR (idProfesor),
    FOREIGN KEY (id_professor_presente) REFERENCES PROFESSOR (idProfesor),
    FOREIGN KEY (id_materia) REFERENCES MATERIA (idMateria)
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def inserirAula(id_turma:int,id_professor_responsavel:int,id_professor_presente:int,id_materia:int,
                data:str,status:bool):
    criarTabelaAula()
    conn, cursor = connect()
    cursor.execute("""
       INSERT INTO AULA(id_turma,id_professor_responsavel,id_professor_presente,id_materia,
                data,status) VALUES(?,?,?,?,?,?)
       """, (id_turma,id_professor_responsavel,id_professor_presente,id_materia,
                         data, status))
    conn.commit()
    cursor.close()
    conn.close()
    print("AULA Add com sucesso! ")


def listarAulas():
    conn, cursor = connect()
    cursor.execute("""
    SELECT T.serie, T.sigla_turma AS 'Turma', PROF_R.nome AS 'PROF RESPONSAVEL',PROF_P.nome AS 'PROF 
    PRESENTE', M.nome, AULA.data,AULA.status
    FROM AULA 
    INNER JOIN TURMA T
    ON T.id = AULA.idAula
    INNER JOIN PROFESSOR PROF_R
    ON PROF_R.idProfesor = AULA.id_professor_responsavel
    INNER JOIN PROFESSOR PROF_P
    ON PROF_P.idProfesor = AULA.id_professor_presente
    INNER JOIN MATERIA M
    ON AULA.id_materia=M.idMateria
    """)
    conn.commit()
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

if __name__ == '__main__':
    inserirAula(1,1,1,2,"21/03/2024",False)
    inserirAula(2, 2, 2, 2, "21/03/2024", False)