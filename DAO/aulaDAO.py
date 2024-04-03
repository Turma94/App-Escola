import mysql.connector
from DAO.turmaDao import *
from DAO.professorDAO import *
from DAO.materiaDAO import *


def conected():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def addAula(serie, sigla, nome, sobrenome, materia, data, n_aula):
    conn, cursor = conected()
    try:
        cursor.execute("""
            INSERT INTO aula (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula) 
            SELECT t.id, p.id, p.id, m.id, %s, %s
            FROM turma t 
            JOIN usuarios p ON p.nome = %s AND p.sobreNome = %s 
            JOIN materia m ON m.nome = %s 
            WHERE t.serie = %s AND t.sigla = %s
            """, (data, n_aula, nome, sobrenome, materia, serie, sigla))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def addAula2(data_aula, numero_aula):
    conn, cursor = conected()
    try:
        cursor.execute("""
            INSERT INTO aula (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula) 
            SELECT t.id, p.id, p.id, m.id, %s, %s 
            FROM turma t 
            JOIN usuarios p ON p.nome = 'nicolas' AND p.sobreNome = 'gama' 
            JOIN materia m ON m.nome = 'Matematica' 
            WHERE t.serie = 9 AND t.sigla = 'N';
        """, (data_aula, numero_aula))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def addAulaTeste(idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula):
    conn, cursor = conected()
    try:
        cursor.execute("""
            INSERT INTO aula (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula) 
            values(%s,%s,%s,%s,%s,%s)
            
            """, (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()








if __name__ == '__main__':
    serie="6"
    sigla="A"
    nome="Tereza"
    sobrenome="Jojo"
    materia="ingles"
    data="2024-04-08"
    n_aula="1"
    id_turma=selecionarTurma(serie,sigla)
    id_prof=selecionarIDDoProfessor(nome,sobrenome)
    id_materia=selecionarMateria(materia)
    print(f"id turma {id_turma}  id prof{id_prof} id materia {id_materia}")


