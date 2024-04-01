import mysql.connector
import datetime as dt


def connect():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123',
        database='escola'
    )
    cursor = conn.cursor()
    return conn, cursor


def inserirTurma(ano_letivo, periodo, serie, sigla_turma):
    conn, cursor = connect()
    try:
        cursor.execute("""INSERT INTO turma (anoLetivo,periodo,serie,sigla)
    VALUES(%s,%s,%s,%s)""", (ano_letivo, periodo, serie, sigla_turma))
        conn.commit()
        print("Turma e registros relacionados adicionados com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao adicionar turma:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def selectTurma():
    conn, cursor = connect()
    cursor.execute("""SELECT * FROM turma """)
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

def selecionarTurma(serie, sigla):
    conn, cursor = connect()
    try:
        cursor.execute("""SELECT id FROM turma WHERE serie = %s AND sigla = %s""", (serie, sigla))
        lista = cursor.fetchall()
        conn.commit()
        print("Turma e registros relacionados buscados com sucesso.")
        return lista
    except mysql.connector.Error as error:
        print("Erro ao buscar turma:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()



def deletarTurma(serie, sigla):
    conn, cursor = connect()
    try:
        cursor.execute("DELETE FROM turma WHERE id IN (SELECT id FROM (SELECT id FROM turma WHERE serie = %s AND "
                       "sigla = %s) AS subquery)", (serie, sigla))
        conn.commit()
        print("Turma e registros relacionados excluídos com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao deletar turma:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

def atualizarTurma(anoLetivo, periodo, serie, sigla, serie_antiga, sigla_antiga):
    conn, cursor = connect()
    try:
        conn, cursor = connect()
        cursor.execute("UPDATE turma SET anoLetivo = %s, periodo = %s, serie = %s, sigla = %s WHERE id IN (SELECT id "
                       "FROM (SELECT id FROM turma WHERE serie = %s AND "
                       "sigla = %s) AS subquery)",
                       (anoLetivo, periodo, serie, sigla, serie_antiga, sigla_antiga))
        conn.commit()
        print("Turma e registros relacionados atualizada com sucesso.")
    except mysql.connector.Error as error:
        print("Erro ao atualizar turma:", error)
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()




if __name__ == '__main__':
    # data=dt.date(2024,7,22)
    # inserirTurma("2024","Tarde","4","A")
    # inserirTurma('2024', "MANHA", "8", "B")
    # inserirTurma("2024", "Tarde", "5", "C")
    # inserirTurma("2024", "Noite", "6", "D")
    # for turma in  selectTurma():
    #    print(turma)
    print(selecionarTurma('8','B'))
    # deletarTurma('2', 'A')
    # atualizarTurma('2023', 'MANHA', '9', 'N', '9','N')
    # print(selectTurma('2','B'))

# def atualizarTurma(**kwargs):
#     conn, cursor = connect()
#     try:
#         for coluna, valor in kwargs.items():
#             cursor.execute(f"SELECT id FROM turma WHERE {coluna} = %s", (valor, ))
#             ids = [registro[0] for registro in cursor.fetchall()]
#
#             for id_registro in ids:
#                 cursor.execute(f"UPDATE turma SET {coluna} = %s WHERE id = %s", (valor, id_registro))
#         conn.commit()
#         print("Turma e registros relacionados atualizados com sucesso.")
#     except mysql.connector.Error as error:
#         print("Erro ao atualizar turma:", error)
#     finally:
#         if 'conn' in locals() and conn.is_connected():
#             conn.commit()
#             cursor.close()
#             conn.close()
