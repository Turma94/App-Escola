import mysql.connector


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
        cursor.execute("""INSERT INTO aula (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula) SELECT %s, id FROM materia WHERE nome LIKE %s (SELECT %s, id FROM usuarios WHERE nome = %s and sobrenome = %s""")
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()