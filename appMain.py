from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
from views.elements.optionsMenuHide import OptionsMenuHide
from views.painels.painelProfessor import PainelProfessor
from views.painels.painelAulas import PainelAula
from views.painels.painelUsuarios import PainelUsuario
from views.painels.painelMateria import PainelMateria
from utils.testarEntradasUsuario import *
from DAO.usuarioDAO import listarUsuario
from utils.criptografia import criptografarSenha
def main(page:Page):

    def openMenuHide(e):
        optionsMenu.open = True
        page.update()
    def change_options_menu_left(e):
        if e.data=="0":
            print("Home")
        elif e.data=="1":
            print("Usuario")
            painelProf.visible = False
            painelProf.update()
            painelMateria.visible = False
            painelMateria.update()
            painelUsuario.visible=True
            painelUsuario.offset = transform.Offset(0, 0)
            painelUsuario.animate_offset = animation.Animation(500)
            painelUsuario.update()
        elif e.data=="2":
            painelMateria.visible = False
            painelMateria.update()
            painelUsuario.visible = False
            painelUsuario.update()
            print("Professores")
            painelProf.visible=True
            painelProf.update()

        elif e.data=="3":
            print("Materia")
            painelProf.visible = False
            painelProf.update()
            painelUsuario.visible = False
            painelUsuario.update()
            painelMateria.visible=True
            painelMateria.offset=transform.Offset(0, 0)
            painelMateria.animate_offset=animation.Animation(500)
            painelMateria.update()
        elif e.data == "4":
            print("Turma")
        elif e.data=="5":
            print("Aulas")
        elif e.data=="6":
            print("Relatorio")
        elif e.data=="7":
            print("Fechar")

    def cadastraUsuario(e):
        pass


    # Views Login
    telaLogin = ViewLogin()
    # View home
    barHome = ViewHome()
    barHome.btn_menu_hide.on_click = openMenuHide

    # Botões escondidos
    optionsMenu = OptionsMenuHide()
    optionsMenu.on_change=change_options_menu_left


    #Painel Professor
    painelProf = PainelProfessor()

    #Painel Aula
    painelAula = PainelAula(page)

    #Painel usuario
    painelUsuario=PainelUsuario()
    painelUsuario.btn_cadastrar.on_click=cadastraUsuario


    #Painel Materia
    painelMateria=PainelMateria()

    #Painel Turma




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
                        painelProf,
                        # painelAula
                        painelUsuario,
                        painelMateria

                    ], drawer=optionsMenu
                )
            )


        page.update()

    page.on_route_change = changeRoutes
    page.go(page.route)


if __name__ == '__main__':
    app(target=main,assets_dir="assets")



