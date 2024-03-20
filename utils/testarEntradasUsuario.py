import re
def testarSenha(senha:str)-> bool:

    regex_senha = r'^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?!.*\s).{8,}$'
    if re.match(regex_senha, senha):
        return True
    else:
        return False


def validar_login(login):
    # Verifica se o login contém apenas letras, números e underscores
    if re.match(r"^\w+$", login):
        return True
    else:
        return False


def validar_email(email):
    # Expressão regular para validar endereços de e-mail
    regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    # Verifica se o e-mail corresponde à expressão regular
    if re.match(regex_email, email):
        return True
    else:
        return False