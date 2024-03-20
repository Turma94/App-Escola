import re
from utils.criptografia import *
from Model.usuarios.usuario import *

############## Login ##############

def validar_email(email):

    # Expressão regular para validar endereços de e-mail

    regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    # Verifica se o e-mail corresponde à expressão regular
    if re.match(regex_email, email):
        return True
    else:
        return False


############## Senha ##############

def criarSenha(senha:str)-> bool:

    regex_senha = r'^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?!.*\s).{8,}$'

    if re.match(regex_senha, senha):
        return True
    else:
        return False

    
def testarSenha(senha:str)-> bool:

    # Verifica se a senha tem 8 caracteres
    if len(senha) == 8:

        return verificaSenha(senha)

    else:

        return False
