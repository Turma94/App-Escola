import mysql.connector


def conected():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def addAula(nome, sobrenome, serie, sigla, materia, data_aula, numero_aula):
    conn, cursor = conected()
    try:
        cursor.execute("""
            SELECT professor.id 
            FROM professor 
            JOIN usuarios ON usuarios.id = professor.idUsuario 
            WHERE usuarios.nome = %s AND usuarios.sobreNome = %s
        """, (nome, sobrenome))
        id_usuario = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO aula (idTurma, idProfessorResponsavel, idProfessorPresente, idMateria, data_aula, numeroAula)
            SELECT t.id, pr.id, pr.id, m.id, %s, %s 
            FROM professor pr      
            JOIN turma t ON t.serie = %s AND t.sigla = %s
            JOIN materia m ON m.nome = %s 
            WHERE pr.id = %s;
        """, (data_aula, numero_aula, serie, sigla, materia, id_usuario))
        conn.commit()
        print("Cadastrado com sucesso!")
    except mysql.connector.Error as error:
        print("Erro ao cadastrar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


def buscarAula(serie, sigla, data_aula):
    conn, cursor = conected()
    try:
        cursor.execute("""
            SELECT * FROM aula a
            JOIN turma t ON t.serie = %s AND t.sigla = %s
            WHERE a.idTurma = t.id AND data_aula = %s
            """, (serie, sigla, data_aula))
        busca = cursor.fetchall()
        return busca
    except mysql.connector.Error as error:
        print("Erro ao buscar aula:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == '__main__':
    pass

    # addAula('nicolas','gama','5', 'B', 'Matematica','2024-9-9',9)
    # print(encontrarProfessor('nicolas', 'gama'))
    print(buscarAula('6', 'A', '2024-12-10'))
