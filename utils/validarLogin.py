from bdTeste import usuarios
#teste
def validarLogin(email):
    has_email = False
    for usuario in usuarios:
        if usuario.email == email:
            has_email = True

    if has_email == True:
        print("login Valido")
        return True
    else:
        print("login invalido")
        return False

validarLogin("caarla@email.com")

