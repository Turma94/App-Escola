from flet import *
import re
from DAO.usuarioDAO import *
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
        regex_nome = r'^[a-zA-Z\s]+$'
        regex_sobreNome = r'^[a-zA-Z\s]+$'
        regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        regex_senha = r"^\d{4}$"

        total_validacoes = 0

        if self.t_field_nome.value != "":
            if re.match(regex_nome, self.t_field_nome.value):
                self.t_field_nome.error_text = ""
                self.t_field_nome.update()
                total_validacoes += 1
            else:
                self.t_field_nome.error_text = "*Nome invalido"
                self.t_field_nome.update()
        else:
            self.t_field_nome.error_text = "*Campo obrigatorio"
            self.t_field_nome.update()


        if self.t_field_sobrenome.value != "":
            if re.match(regex_sobreNome, self.t_field_sobrenome.value):
                self.t_field_sobrenome.error_text = ""
                self.t_field_sobrenome.update()
                total_validacoes += 1
            else:
                self.t_field_sobrenome.error_text = "*SobreNome invalido"
                self.t_field_sobrenome.update()
        else:
            self.t_field_sobrenome.error_text = "*Campo obrigatorio"
            self.t_field_sobrenome.update()


        if self.t_field_email.value != "":
            if re.match(regex_email, self.t_field_email.value):

                has_email = False

                for usuario in listarUsuario():
                    if usuario[4] == self.t_field_email.value:
                        has_email = True

                if has_email == False:
                    self.t_field_email.error_text = ""
                    self.t_field_email.update()
                    total_validacoes += 1
                else:
                    self.t_field_email.error_text = "Email ja cadastrado"
                    self.t_field_email.update()

            else:
                self.t_field_email.error_text = "*Email invalido"
                self.t_field_email.update()
        else:
            self.t_field_email.error_text = "*Campo obrigatorio"
            self.t_field_email.update()


        if self.t_field_senha.value != "":
            if len(self.t_field_senha.value) == 4:
                if re.match(regex_senha, self.t_field_senha.value):
                    self.t_field_senha.error_text = ""
                    self.t_field_senha.update()
                    total_validacoes += 1
                else:
                    self.t_field_senha.error_text = "*A senha deve conter apenas 4 caracteres numericos"
                    self.t_field_senha.update()
            else:
                self.t_field_senha.error_text = "*A senha teve coneter 4 caracteres"
                self.t_field_senha.update()
        else:
            self.t_field_senha.error_text = "*Campo obrigatorio"
            self.t_field_senha.update()


        if self.drop_nivel.value != None:
            self.drop_nivel.error_text = ""
            self.drop_nivel.update()
            total_validacoes += 1
        else:
            self.drop_nivel.error_text = "*campo obrigatorio"
            self.drop_nivel.update()


        if total_validacoes == 5:

            #addUsuario(self.t_field_nome.value,self.t_field_sobrenome.value,self.t_field_senha.value,self.t_field_email.value,self.drop_nivel.value)



            self.t_field_nome.value = ""
            self.t_field_nome.update()

            self.t_field_sobrenome.value = ""
            self.t_field_sobrenome.update()

            self.t_field_email.value = ""
            self.t_field_email.update()

            self.t_field_senha.value = ""
            self.t_field_senha.update()

            self.drop_nivel.value = None
            self.drop_nivel.update()

            print("sucesso")







