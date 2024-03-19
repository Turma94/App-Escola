import re
def testarSenha(senha:str)-> bool:

    regex_senha= r'^.*\d{4}.*$'
    if re.match(regex_senha,senha):
        return True
    else:
        return False



