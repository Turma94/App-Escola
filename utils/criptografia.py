from hashlib import sha256

def criptografarSenha(senha):
    senha = sha256(senha.encode())
    return senha.hexdigest()

senhaBanco = ["12345678", "01234567", "1234567a"]
senhaBanco[0] = sha256(senhaBanco[0].encode())
senhaBanco[1] = sha256(senhaBanco[1].encode())
senhaBanco[2] = sha256(senhaBanco[2].encode())
###############################

def verificaSenha(senha):

    senha = sha256(senha.encode())

    hasSenha = False
    for BDSenhas in senhaBanco:
        if BDSenhas.hexdigest() == senha.hexdigest():
            hasSenha = True

    if hasSenha == True:
        print("bem vindo")
        return True
    else:
        print("Senha invalida")
        return False

verificaSenha("1234567")