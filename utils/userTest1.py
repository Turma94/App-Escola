# # Usuários e seus respectivos emails
# usuarios_emails = [
#     ("Kayla", "Moore", "senha1", "kaylamoore@example.net", "COMUM"),
#     ("Rivera", "Debra", "senha2", "riveradebra@example.net", "COMUM"),
#     ("Audrey", "Whitaker", "senha3", "audreywhitaker@example.net", "COMUM"),
#     # E assim por diante para os outros emails
#     ("Steven", "Williams", "senhaN", "stevenwilliams@example.net", "COMUM"),
#     ("Larson", "Michael", "senhaN", "larsonmichael@example.com", "COMUM")
# ]
#
# # Modificar a função addUsuario para aceitar uma lista de tuplas contendo os dados dos usuários
# def addUsuarios(usuarios):
#     criarTabelaUsuario()
#     conn, cursor = connect()
#     for usuario in usuarios:
#         cursor.execute("""
#             INSERT INTO USUARIO (nome, sobrenome, senha, email, nivel)
#             VALUES (?, ?, ?, ?, ?)
#         """, usuario)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     print("Usuários cadastrados com sucesso!")
#
# # Chamar a função addUsuarios com a lista de usuários e emails
# addUsuarios(usuarios_emails)

from faker import Faker

def gerar_usuarios(range_size=100):
    fake = Faker()
    usuarios = []
    for _ in range(range_size):
        nome = fake.first_name()
        sobrenome = fake.last_name()
        email = fake.email()
        senha = fake.password()
        usuario = {
            "nome": nome,
            "sobrenome": sobrenome,
            "email": email,
            "senha": senha
        }
        usuarios.append(usuario)
    return usuarios

# Exemplo de uso
usuarios_gerados = gerar_usuarios()
for usuario in usuarios_gerados:
    print(usuario)

# import faker
# import pandas as pd
#
# def criar_usuarios_fake(numero_de_usuarios):
#     fake = faker.Faker()
#     usuarios = []
#     for _ in range(numero_de_usuarios):
#         nome = fake.first_name()
#         sobrenome = fake.last_name()
#         email = fake.email()
#         senha = fake.password()
#         usuarios.append({'Nome': nome, 'Sobrenome': sobrenome, 'Email': email, 'Senha': senha})
#     return usuarios
#
# def exportar_para_excel(usuarios, nome_arquivo):
#     df = pd.DataFrame(usuarios)
#     df.to_excel(nome_arquivo, index=False)
#
# if __name__ == "__main__":
#     numero_de_usuarios = 100
#     usuarios = criar_usuarios_fake(numero_de_usuarios)
#     exportar_para_excel(usuarios, 'usuarios_fake.xlsx')

# from faker import Faker
# import sqlite3
#
# fake = Faker()
#
# def criar_usuarios(num_usuarios):
#     conn = sqlite3.connect('usuarios.db')
#     c = conn.cursor()
#
#     c.execute('''CREATE TABLE IF NOT EXISTS usuarios
#                  (id INTEGER PRIMARY KEY,
#                  nome TEXT,
#                  sobrenome TEXT,
#                  email TEXT,
#                  senha TEXT)''')
#
#     for _ in range(num_usuarios):
#         nome = fake.first_name()
#         sobrenome = fake.last_name()
#         email = fake.email()
#         senha = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
#         c.execute("INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES (?, ?, ?, ?)",
#                   (nome, sobrenome, email, senha))
#
#
#
#     conn.commit()
#     conn.close()
#
# criar_usuarios(100)

