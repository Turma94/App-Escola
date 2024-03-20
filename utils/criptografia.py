from hashlib import sha256
from bdTeste import usuarios
#teste
def criptografarSenha(senha):
    senha = sha256(senha.encode())
    return senha.hexdigest()

def verificaSenha(senha):

    senha = sha256(senha.encode())

    hasSenha = False
    for usurio in usuarios:
        has_senha = sha256(usurio.senha.encode())
        if has_senha.hexdigest() == senha.hexdigest():
            hasSenha = True

    if hasSenha == True:
        print("bem vindo")
        return True
    else:
        print("Senha invalida")
        return False