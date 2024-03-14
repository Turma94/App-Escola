from flet import *
from views.viewLogin import ViewLogin

def main(page:Page):


    telaLogin=ViewLogin()

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
                        Text("Sei la pagina")

                    ]
                )
            )


        page.update()

    page.on_route_change=changeRoutes
    page.go(page.route)





if __name__ == '__main__':
    app(target=main,assets_dir="assets")



