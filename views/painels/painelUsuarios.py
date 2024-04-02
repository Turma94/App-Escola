from flet import *
import re
from DAO.usuarioDAO import *
from utils.criptografia import criptografarSenha

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
                                       dropdown.Option("ADMINISTRADOR"),
                                       dropdown.Option("GERENCIA")
                                   ])
        self.btn_cadastrar = FilledButton(text="CADASTRAR", width=250, height=50, style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20), on_click=self.validarCamposCadastro)


        self.list_view_table_cartridges = GridView(expand=1, spacing=0, padding=0, height=400)

        # Estou criando a tabela
        self.tabela = DataTable(
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("Nome")),
                DataColumn(Text("Sobrenome")),
                DataColumn(Text("Email")),
                DataColumn(Text("Nível")),
                DataColumn(Text("Status"))
            ],
            expand=True,
            show_checkbox_column=True,
            sort_column_index=0,
            sort_ascending=True,
            on_select_all=True

        )

        self.list_view_table_cartridges.controls.append(self.tabela)

        self.content=Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Column(controls=[

                Row(controls=[Container(content=self.subtitulo, border=border.all(2, "#9A9A9A"), width=1010, height=60, margin=40, alignment=alignment.center)],
                    alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_nome, self.t_field_sobrenome], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_email], alignment=MainAxisAlignment.CENTER),

                Row(controls=[self.t_field_senha, self.drop_nivel], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.btn_cadastrar], alignment=MainAxisAlignment.SPACE_AROUND),
                Row(controls=[self.list_view_table_cartridges],alignment=MainAxisAlignment.CENTER)

            ], alignment=MainAxisAlignment.CENTER)

        ], alignment=MainAxisAlignment.SPACE_AROUND)


        self.offset = transform.Offset(0, 0)
        self.animate_offset = animation.Animation(500)
        self.visible = False

        self.carregarTabela()

    def validarCamposCadastro(self, e):
        regex_nome = r'^[a-zA-Z\s]+$'
        regex_sobreNome = r'^[a-zA-Z\s]+$'
        regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
        regex_senha = r"^\d{4}$"

        total_validacoes = 0

        print(self.drop_nivel.value)

        if self.t_field_nome.value != "":
            if re.match(regex_nome, self.t_field_nome.value.replace(" ", "").capitalize()):
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
            if re.match(regex_sobreNome, self.t_field_sobrenome.value.replace(" ", "").capitalize()):
                self.t_field_sobrenome.error_text = ""
                self.t_field_sobrenome.update()
                total_validacoes += 1
            else:
                self.t_field_sobrenome.error_text = "*Sobrenome invalido"
                self.t_field_sobrenome.update()
        else:
            self.t_field_sobrenome.error_text = "*Campo obrigatorio"
            self.t_field_sobrenome.update()


        if self.t_field_email.value != "":
            if re.match(regex_email, self.t_field_email.value.replace(" ", "")):

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
            print(self.drop_nivel.value)
            self.drop_nivel.error_text = ""
            self.drop_nivel.update()
            total_validacoes += 1
        else:
            self.drop_nivel.error_text = "*campo obrigatorio"
            self.drop_nivel.update()


        if total_validacoes == 5:

            # print(self.drop_nivel.value)

            addUsuario(self.t_field_nome.value.replace(" ", "").capitalize(),
                       self.t_field_sobrenome.value.replace(" ", "").capitalize(),
                       criptografarSenha(self.t_field_senha.value),
                       self.t_field_email.value,
                       self.drop_nivel.value, "False")

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
            self.tabela.rows.clear()
            self.carregarTabela()
            self.tabela.update()

            print("sucesso")


    # estou carregando os dados para a tabela
    def carregarTabela(self):


        for usuario in listarUsuario():
            self.tabela.rows.append(DataRow(
                                        data="seila",
                                        cells=[
                                            DataCell(Text(usuario[0])),
                                            DataCell(Text(usuario[1])),
                                            DataCell(Text(usuario[2])),
                                            DataCell(Text(usuario[4])),
                                            DataCell(Text(usuario[5])),
                                            DataCell(Text(usuario[6])),

                                        ], on_select_changed=lambda e: print(f"linha selecionado: {e}"


                                        )))





