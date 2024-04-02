from flet import *
import re
from DAO.turmaDao import *
import datetime

class PainelTurma(Container):
    def __init__(self):
        super().__init__()
        # Título
        self.titulo = Text("Gerenciamento de Turma", size=30)
        # Subtitulo
        self.subtitulo = Text("NOVA TURMA", size=25, text_align=TextAlign.CENTER)
        # Cadastro
        self.drop_turma = Dropdown(label="Turma", width=300,
                                   options=[
                                       dropdown.Option("1°"), dropdown.Option("2°"),
                                       dropdown.Option("3°"), dropdown.Option("5ª"),
                                       dropdown.Option("6ª"), dropdown.Option("7ª"),
                                       dropdown.Option("8ª"), dropdown.Option("9°")
                                   ])
        self.drop_sigla = Dropdown(label="Sigla", width=300,
                                   options=[
                                       dropdown.Option("A"), dropdown.Option("B"),
                                       dropdown.Option("C"), dropdown.Option("D"),
                                       dropdown.Option("E"), dropdown.Option("F"),
                                       dropdown.Option("G"), dropdown.Option("H")
                                   ])
        self.drop_periodo = Dropdown(label="Periodo", width=300,
                                     options=[
                                         dropdown.Option("Manhã"),
                                         dropdown.Option("Tarde"),
                                         dropdown.Option("Noite")
                                     ])
        self.t_field_ano_letivo = TextField(label="Ano Letivo", width=300)

        self.list_view_table_cartridges = GridView(expand=1, spacing=0, padding=0, height=400)

        self.btn_cadastrar = FilledButton(text="CADASTRAR", width=250, height=50, style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20), on_click=self.cadastraTurma)

        self.tabela = DataTable(
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("Ano Letivo")),
                DataColumn(Text("Periodo")),
                DataColumn(Text("Série")),
                DataColumn(Text("Sigla")),

            ],
            expand=True,
            show_checkbox_column=True,
            sort_column_index=0,
            sort_ascending=True,
            on_select_all=True

        )


        self.list_view_table_cartridges.controls.append(self.tabela)

        self.content = Column (  controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Column(controls=[
                Row(controls=[
                    Container(content=self.subtitulo, border=border.all(2, "#9A9A9A"), width=1010, height=60, margin=40,
                              alignment=alignment.center)],
                    alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.drop_turma, self.drop_sigla], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_ano_letivo, self.drop_periodo], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.btn_cadastrar], alignment=MainAxisAlignment.SPACE_AROUND),
                Row(controls=[self.list_view_table_cartridges], alignment=MainAxisAlignment.CENTER)
            ], alignment=MainAxisAlignment.CENTER),


        ],alignment=MainAxisAlignment.SPACE_AROUND)
        self.offset = transform.Offset(0, 0)
        self.animate_offset = animation.Animation(500)
        self.visible = False
        self.carregarTabela()


    def cadastraTurma(self, e):

        totalValidacoes = 0

        if self.drop_turma.value != None:
            self.drop_turma.error_text = ""
            self.drop_turma.update()
            totalValidacoes += 1
        else:
            self.drop_turma.error_text = "*Campo obrigatorio"
            self.drop_turma.update()

        if self.drop_sigla.value != None:
            self.drop_sigla.error_text = ""
            self.drop_sigla.update()
            totalValidacoes += 1
        else:
            self.drop_sigla.error_text = "*Campo obrigatorio"
            self.drop_sigla.update()

        if self.drop_periodo.value != None:
            self.drop_periodo.error_text = ""
            self.drop_periodo.update()
            totalValidacoes += 1
        else:
            self.drop_periodo.error_text = "*Campo obrigatorio"
            self.drop_periodo.update()

        if self.t_field_ano_letivo.value != "":
            regex_senha = r"^\d{4}$"

            if re.match(regex_senha, self.t_field_ano_letivo.value):

                if int(self.t_field_ano_letivo.value) >= datetime.datetime.now().year:
                    self.t_field_ano_letivo.error_text = ""
                    self.t_field_ano_letivo.update()
                    totalValidacoes += 1
                else:
                    self.t_field_ano_letivo.error_text = f"*A data não pode ser menor que {datetime.datetime.now().year}"
                    self.t_field_ano_letivo.update()
            else:
                self.t_field_ano_letivo.error_text = "*Deve conter apenas numeros"
                self.t_field_ano_letivo.update()
        else:
            self.t_field_ano_letivo.error_text = "*Campo obrigatorio"
            self.t_field_ano_letivo.update()

        tema_turma = False

        for turma in selectTurma():
            # (1, datetime.date(2024, 3, 26), 'MANHA', '1', 'B')
            if (self.drop_turma.value == turma[3]
                    and self.drop_sigla.value == turma[4]
                    and self.drop_periodo.value == turma[2]):
                print(turma[3], turma[4], turma[2])
                tema_turma = True

        if totalValidacoes == 4:

            #inserirTurma(ano_letivo, periodo, serie, sigla_turma)

            if tema_turma == True:
                self.t_field_ano_letivo.error_text = "*turma ja cadastrada"
                self.t_field_ano_letivo.update()
                print("*turma ja cadastrada")
            else:
                inserirTurma(self.t_field_ano_letivo.value, self.drop_periodo.value, self.drop_turma.value, self.drop_sigla.value)
                self.drop_turma.error_text = ""
                self.drop_turma.update()
                self.drop_sigla.error_text = ""
                self.drop_sigla.update()
                self.drop_periodo.error_text = ""
                self.drop_periodo.update()
                self.t_field_ano_letivo.error_text = ""
                self.t_field_ano_letivo.update()
                self.tabela.rows.clear()
                self.carregarTabela()
                self.tabela.update()

 # estou carregando os dados para a tabela
    def carregarTabela(self):

        for turma in selectTurma():
            self.tabela.rows.append(DataRow(
                                        data="seila",
                                        cells=[
                                            DataCell(Text(turma[0])),
                                            DataCell(Text(turma[1])),
                                            DataCell(Text(turma[2])),
                                            DataCell(Text(turma[3])),
                                            DataCell(Text(turma[4]))


                                        ], on_select_changed=lambda e: print(f"linha selecionado: {e}"


                                        )))