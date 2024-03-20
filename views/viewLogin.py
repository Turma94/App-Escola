from flet import *


class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.logo = Image(src=r"logotipo.png")
        self.titleView = Text("LOGIN", color="#060457", size=38)
        self.t_fild_login = TextField(label="Usuario")
        self.t_fild_passWord = TextField(label="Senha")

        self.btn_enter = ElevatedButton("ENTRAR", style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20))


    def build(self):
        lineBtn = ResponsiveRow(col={"xs": 6, "sm": 2, "md": 3}, controls=[self.btn_enter], alignment=MainAxisAlignment.CENTER)
        layout = ResponsiveRow(
            controls=[
               Column(col={"xs": 8, "sm": 6, "md": 4}, controls=[self.logo], alignment=alignment.center),
               Row(controls=[self.titleView], alignment=MainAxisAlignment.CENTER),

               Column(col={"xs": 10, "sm": 8, "md": 6, "lg": 4}, controls=[
                   self.t_fild_login,
                   self.t_fild_passWord,
                   lineBtn], alignment=MainAxisAlignment.CENTER),

            ], alignment=MainAxisAlignment.CENTER)




        return layout
