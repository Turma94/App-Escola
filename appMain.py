from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
def main(page:Page):



    optionsMenu=NavigationDrawer(
        controls=[
            NavigationDrawerDestination(
                label="Home",
                icon=icons.HOME,
                selected_icon_content=Icon(icons.HOME_OUTLINED),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                label="Professores",
                icon=icons.PERSON_ADD_ALT_SHARP,
                selected_icon_content=Icon(icons.PERSON_ADD_ALT_OUTLINED),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                label="Matérias",
                icon=icons.ASSIGNMENT,
                selected_icon_content=Icon(icons.ASSIGNMENT),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                label="Aulas",
                icon=icons.CALENDAR_TODAY,
                selected_icon_content=Icon(icons.CALENDAR_TODAY_OUTLINED),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                label="Relatório",
                icon=icons.FOLDER,
                selected_icon_content=Icon(icons.FOLDER_OUTLINED),
            ),
            Divider(thickness=2),
            NavigationDrawerDestination(
                label="Sair",
                icon=icons.EXIT_TO_APP,
                selected_icon_content=Icon(icons.EXIT_TO_APP),
            ),

        ]
    )

    def openMenuHide(e):
        optionsMenu.open=True
        page.update()


    telaLogin=ViewLogin()
    barHome=ViewHome()
    barHome.btn_menu_hide.on_click= openMenuHide

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
                        barHome

                    ], drawer=optionsMenu
                )
            )


        page.update()

    page.on_route_change=changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main,assets_dir="assets")



