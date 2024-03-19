from flet import *
from turmaDao import selectTurma
from datetime import datetime

class PainelAula(UserControl):

    def __init__(self,page):
        super().__init__()
        self.page=page
        self.text_data_inicio=Text(value="Data Inicial")

        self.data_inicial = DatePicker(
            on_change=self.modificarDataInicial,
            first_date=datetime(2023, 10, 1),
            last_date=datetime(2050, 10, 1),
        )

        self.quantidadeDias=TextField(label="Dias à lançar")

        self.tabelaAula=DataTable(
            columns=[
                DataColumn(Text("Seg")),
                DataColumn(Text("Ter")),
                DataColumn(Text("Qua")),
                DataColumn(Text("Qui")),
                DataColumn(Text("Sex")),
                DataColumn(Text("Sab")),
            ],

        )


    def modificarDataInicial(self,e):
        self.text_data_inicio.value=(f"{self.data_inicial.value.day}/{self.data_inicial.value.month}/"
                                    f"{self.data_inicial.value.year}")
        self.text_data_inicio.update()



    def build(self):
        self.titulo = Text("Gerenciamento de Aulas", size=30)


        self.page.overlay.append(self.data_inicial)

        self.drop_turma = Dropdown(label="Turma")


        for turma in selectTurma():
            self.drop_turma.options.append(dropdown.Option(f"{turma[3]} {turma[4]}"))




        # Tentando colcoar as coisas dentro de uma grid
        self.grid_list_aulas=GridView(expand=True, max_extent=150, child_aspect_ratio=1)

        self.list_aulas = Column(alignment=MainAxisAlignment.CENTER)
        linhaDataInicio=Row(controls=[IconButton(icon=icons.CALENDAR_TODAY, on_click= lambda
                  e: self.data_inicial.pick_date()), self.text_data_inicio])

        linhaDiasLancar = Row(controls=[self.quantidadeDias])

        return Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Row(controls=[
                Row(controls=[
                    self.drop_turma,
                    linhaDataInicio,
                    linhaDiasLancar

                             ]),
                FloatingActionButton(icon=icons.CHECK, on_click=self.add_clicked)], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            self.tabelaAula,
            self.list_aulas
        ])




    def add_clicked(self, e):
        self.list_aulas.controls.append(

            Column(controls=[


                Divider(thickness=2),
            #     Vou colocar uma tab aqui para mostrar as semanas


            ]))



        self.update()








class NewAula(UserControl):

    def __init__(self, periodo, turma, tipo):
        super().__init__()
        self.periodo = periodo
        self.turma = turma
        self.tipo = tipo


    def build(self):
        self.display_aula = Checkbox(value=False, label=f"{self.periodo} | {self.turma} | {self.tipo}")

        self.edit_periodo = Dropdown(label="Período",
                                     options=[
                                       dropdown.Option("Manhã"),
                                       dropdown.Option("Tarde"),
                                       dropdown.Option("Noite")
                                     ])

        self.edit_turma = Dropdown(label="Turma",
                                   options=[
                                       dropdown.Option("1-A"),
                                       dropdown.Option("1-B"),
                                       dropdown.Option("2-A"),
                                       dropdown.Option("2-B")
                                   ])

        self.tipo = Dropdown(label="Tipo",
                                   options=[
                                       dropdown.Option("Semana"),
                                       dropdown.Option("Mês"),
                                       dropdown.Option("Semestre")
                                   ])


        self.display_view = Row(controls=[
            self.display_aula
        ])


        return Column(controls=[self.display_aula])









