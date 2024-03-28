from flet import *
import re
class PainelUsuario(Container):

    def __init__(self):
        super().__init__()
        # Título
        self.titulo = Text("Gerenciamento de Usuários", size=30)
        # Subtitulo
        self.subtitulo = Text("NOVO USUÁRIO", size=25, text_align=TextAlign.CENTER)
        # Cadastro
        self.t_field_nome = TextField(label="Nome", width=500)
        self.t_field_sobrenome = TextField(label="Sobrenome", width=500)
        self.t_field_email = TextField(label="Email", width=1010)
        self.t_field_senha = TextField(label="Senha", width=500, password=True, can_reveal_password=True)
        self.drop_nivel = Dropdown(label="Nível", width=500,
                                   options=[
                                       dropdown.Option("COMUM"),
                                       dropdown.Option("ADM"),
                                       dropdown.Option("GERENTE")
                                   ])
        self.btn_cadastrar = FilledButton(text="CADASTRAR", width=250, height=50, style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20), on_click=self.validarCamposCadastro)

        self.content=Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Column(controls=[

                Row(controls=[Container(content=self.subtitulo, border=border.all(2, "#9A9A9A"), width=1010, height=60, margin=40, alignment=alignment.center)],
                    alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_nome, self.t_field_sobrenome], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_email], alignment=MainAxisAlignment.CENTER),

                Row(controls=[self.t_field_senha, self.drop_nivel], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.btn_cadastrar], alignment=MainAxisAlignment.SPACE_AROUND)

            ], alignment=MainAxisAlignment.CENTER)

        ], alignment=MainAxisAlignment.SPACE_AROUND)

        self.offset = transform.Offset(0, 0)
        self.animate_offset = animation.Animation(500)
        self.visible = False

    def validarCamposCadastro(self, e):
        # Define a expressão regular para verificar se há apenas letras (maiúsculas e minúsculas) e espaços
        regex_nome = r'^[a-zA-Z\s]+$'
        regex_sobreNome = r'^[a-zA-Z\s]+$'
        regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        # Verifica se os dados correspondem ao padrão

        if re.match(regex_nome, self.t_field_nome.value):
            self.t_field_nome.error_text = ""
            self.t_field_nome.update()

            if re.match(regex_sobreNome, self.t_field_sobrenome.value) and self.t_field_sobrenome.value.strip() != "":
                self.t_field_sobrenome.error_text = ""
                self.t_field_sobrenome.update()

                if re.match(regex_email, self.t_field_email.value):
                    self.t_field_email.error_text = ""
                    self.t_field_email.update()

                else:
                    self.t_field_email.error_text = "email invalido"
                    self.t_field_email.update()


            else:
                self.t_field_sobrenome.error_text = "sobreNome invalido"
                self.t_field_sobrenome.update()

        else:
            self.t_field_nome.error_text = "Nome invalido"
            self.t_field_nome.update()
            return False




