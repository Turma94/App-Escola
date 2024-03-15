from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
def main(page:Page):



    optionsMenu=NavigationDrawer(
        controls=[
            NavigationDrawerDestination(
                label="Item 1",
                icon=icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=Icon(icons.DOOR_BACK_DOOR),
            ),
        ]
    )

    telaLogin=ViewLogin()
    barHome=ViewHome()
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

                    ]
                )
            )


        page.update()

    page.on_route_change=changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main,assets_dir="assets")



