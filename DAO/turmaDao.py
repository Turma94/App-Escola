import mysql.connector
import datetime as dt
def connect():


    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )
    cursor=conn.cursor()
    return conn, cursor







def inserirTurma(ano_letivo,periodo,serie,sigla_turma):

    conn, cursor = connect()
    cursor.execute("""INSERT INTO turma (anoLetivo,periodo,serie,sigla)
    VALUES(?,?,?,?)
    """,(ano_letivo,periodo,serie,sigla_turma))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add com sucesso !")


def selectTurma():
    conn, cursor = connect()
    cursor.execute("""SELECT * FROM turma """)
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista





if __name__ == '__main__':

    data=dt.date(2024,7,22)
    # inserirTurma("2024","Tarde","4","A")
    # inserirTurma(data, "MANHA", "8", "B")
    # inserirTurma("2024", "Tarde", "5", "C")
    # inserirTurma("2024", "Noite", "6", "D")
    for turma in  selectTurma():
       print(turma)