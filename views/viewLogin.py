from flet import *


class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.logo=Image(src=r"logotipo.png")
        self.titleView=Text("LOGIN")
        self.t_fild_login=TextField(label="Usuario")
        self.t_fild_passWord = TextField(label="Senha")
        self.btn_enter=ElevatedButton("ENTRAR")

    def build(self):

        layout=ResponsiveRow(
            controls=[
               Column(controls=[self.logo]),
               Row(controls=[self.titleView]),
               Column(controls=[self.t_fild_login]),
               Column(controls=[self.t_fild_passWord]),
               Column(controls=[self.btn_enter])
            ]
        )




        return layout
