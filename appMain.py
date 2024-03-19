from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
from views.elements.optionsMenuHide import OptionsMenuHide
from views.painels.painelProfessor import PainelProfessor
from views.painels.painelAulas import PainelAula

def main(page:Page):

    def openMenuHide(e):
        optionsMenu.open=True
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



    telaLogin.btn_enter.on_click=lambda e: page.go("/home")

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

    page.on_route_change=changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main,assets_dir="assets")



