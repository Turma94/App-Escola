from hashlib import sha256
from hashlib import sha256

def criptografarSenha(senha):
    senha = sha256(senha.encode())
    return senha.hexdigest()

if __name__ == '__main__':

    senha="1234"
    hash_senha=sha256(senha.encode())
    print(hash_senha.hexdigest())


    senhaDigitada=input("digite sua senha: ")
    hash_senha_digitada=sha256(senhaDigitada.encode())

    if hash_senha.digest()==hash_senha_digitada.digest():
        print("Validado")
    else:
        print("Validado")