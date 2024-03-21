from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
from views.elements.optionsMenuHide import OptionsMenuHide
from views.painels.painelProfessor import PainelProfessor
from views.painels.painelAulas import PainelAula
from utils.testarEntradasUsuario import *
from usuarioDAO import listarUsuario
from utils.criptografia import criptografarSenha
def main(page:Page):

    def openMenuHide(e):
        optionsMenu.open = True
        page.update()

    # Views Login
    telaLogin = ViewLogin()
    # View home
    barHome = ViewHome()
    barHome.btn_menu_hide.on_click = openMenuHide
    optionsMenu = OptionsMenuHide()

    #Painel Professor
    painelProf = PainelProfessor()

    #Painel Aula
    painelAula = PainelAula(page)

    # Depois tirar essa função e colocar na controller 
    def entrarSistema(e):

        if validar_email(telaLogin.t_fild_login.value):
            for usuario in listarUsuario():

                if usuario[4]==telaLogin.t_fild_login.value:
                    telaLogin.t_fild_login.error_text = ""
                    telaLogin.t_fild_login.update()

                    if testarSenha(telaLogin.t_fild_passWord.value):
                        senhaCript=criptografarSenha(telaLogin.t_fild_passWord.value)
                        telaLogin.t_fild_passWord.error_text = ""
                        telaLogin.t_fild_passWord.update()
                        if senhaCript==usuario[3]:


                            page.go("/home")
                        else:
                            telaLogin.t_fild_passWord.error_text = "Sua senha não esta cadastrada"
                            telaLogin.t_fild_passWord.update()
                    else:
                        telaLogin.t_fild_passWord.error_text = "A senha deve conter 8 caracteres!"
                        telaLogin.t_fild_passWord.update()
        else:
            telaLogin.t_fild_login.error_text = "Este não é uma E-mail não valido"
            telaLogin.t_fild_login.update()


    telaLogin.btn_enter.on_click=entrarSistema

    def changeRoutes(route):
        page.views.clear()

        page.views.append(
            View(
               route="/",
               controls=[
                  telaLogin

            ]
            )
        )

        if page.route=="/home":
            page.views.append(
                View(
                    route="/home",
                    controls=[
                        barHome,
                        #painelProf
                        painelAula

                    ], drawer=optionsMenu
                )
            )


        page.update()

    page.on_route_change = changeRoutes
    page.go(page.route)


if __name__ == '__main__':
    app(target=main,assets_dir="assets")



