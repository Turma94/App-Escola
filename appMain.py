from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
from views.elements.optionsMenuHide import OptionsMenuHide
from views.painels.painelProfessor import PainelProfessor
from views.painels.painelAulas import PainelAula
from views.painels.painelUsuarios import PainelUsuario
from views.painels.painelMateria import PainelMateria
from views.painels.painelTurma import PainelTurma
from views.painels.painelAulaMatriz import PainelAulaMatriz
from views.painels.painelHome import PainelHome
def main(page:Page):

    page.window_min_width=1100
    page.window_min_height=900
    def fecharPaineis(args):
        for painel in args:
            painel.visible = False
            painel.update()

    def openMenuHide(e):
        optionsMenu.open = True
        page.update()

    #     Aqui modificamos os paineis
    def change_options_menu_left(e):
        if e.data == "0":
            print("Home")

        elif e.data == "1":
            print("Usuario")
            fecharPaineis([painelProf, painelMateria,painelAula,painelTurma])
            painelUsuario.visible = True
            painelUsuario.update()

        elif e.data == "2":
            print("Professores")
            fecharPaineis([painelUsuario, painelMateria,painelTurma,painelAula])
            painelProf.visible = True
            painelProf.update()

        elif e.data == "3":
            print("Materia")
            fecharPaineis([painelUsuario, painelProf,painelAula,painelTurma])
            painelMateria.visible = True
            painelMateria.update()

        elif e.data == "4":
            fecharPaineis([painelUsuario, painelProf,painelMateria, painelAula])
            painelTurma.visible = True
            painelTurma.update()
            print("Turma")

        elif e.data == "5":
            print("Aulas")
            fecharPaineis([painelMateria,painelProf,painelUsuario,painelTurma])
            painelAula.visible = True
            painelAula.update()

        elif e.data == "6":
            print("Relatorio")

        elif e.data == "7":
            print("Fechar")

    # Views Login
    telaLogin = ViewLogin()

    # View home
    barHome = ViewHome()
    barHome.btn_menu_hide.on_click = openMenuHide

    # Botões de Acesso aos paineis
    optionsMenu = OptionsMenuHide()
    optionsMenu.on_change=change_options_menu_left


    # Painel Home
    painelHome=PainelHome()

    #Painel Professor
    painelProf = PainelProfessor()
    painelProf.visible=False

    #Painel Aula
    painelAula = PainelAulaMatriz(page)


    #Painel usuario
    painelUsuario=PainelUsuario()
    painelUsuario.btn_cadastrar.on_click = painelUsuario.validarCamposCadastro


    #Painel Materia
    painelMateria=PainelMateria()
    painelMateria.visible=False

    #Painel Turma
    painelTurma=PainelTurma()


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
                        painelHome,
                        painelProf,
                        painelAula,
                        painelUsuario,
                        painelMateria,
                        painelTurma

                    ], drawer=optionsMenu
                )
            )


        page.update()

    page.on_route_change = changeRoutes
    page.go(page.route)


if __name__ == '__main__':
    app(target=main, assets_dir="assets")



