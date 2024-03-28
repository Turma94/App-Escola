from flet import *
from utils.testarEntradasUsuario import *
from DAO.usuarioDAO import listarUsuario
from utils.criptografia import criptografarSenha

class ViewLogin(UserControl):

    def __init__(self):
        super().__init__()
        self.logo = Image(src=r"logotipo.png")
        self.titleView = Text("LOGIN", color="#060457", size=38)
        self.t_fild_login = TextField(label="Usuario")
        self.t_fild_passWord = TextField(label="Senha",password=True,can_reveal_password=True)

        self.btn_enter = ElevatedButton("ENTRAR", style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20), on_click=self.entrarSistema)


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

    # Função valida as entradas para entrar no sistema
    def entrarSistema(self, e):

        if validar_email(self.t_fild_login.value):
            for usuario in listarUsuario():

                if usuario[4]==self.t_fild_login.value:
                    self.t_fild_login.error_text = ""
                    self.t_fild_login.update()

                    if testarSenha(self.t_fild_passWord.value):
                        senhaCript = criptografarSenha(self.t_fild_passWord.value)
                        self.t_fild_passWord.error_text = ""
                        self.t_fild_passWord.update()
                        if senhaCript == usuario[3]:

                            self.page.go("/home")

                        else:
                            self.t_fild_passWord.error_text = "Sua senha não esta cadastrada"
                            self.t_fild_passWord.update()
                    else:
                        self.t_fild_passWord.error_text = "A senha deve conter 8 caracteres!"
                        self.t_fild_passWord.update()
        else:
            self.t_fild_login.error_text = "Este não é uma E-mail não valido"
            self.t_fild_login.update()