from flet import *
from turmaDao import selectTurma
from datetime import datetime
from materiaDAO import listarMaterias


class PainelAula(UserControl):

    def __init__(self,page):
        super().__init__()
        self.page=page
        self.text_data_inicio=Text(value="Escolher dia")

        self.data_inicial = DatePicker(
            on_change=self.modificarDataInicial,
            first_date=datetime(2023, 10, 1),
            last_date=datetime(2050, 10, 1),
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



        return Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Row(controls=[
                Row(controls=[
                    self.drop_turma,
                    linhaDataInicio,


                             ]),
                FloatingActionButton(icon=icons.CHECK, on_click=self.add_clicked)], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),

            self.list_aulas
        ])



    def add_clicked(self, e):
        self.list_aulas.controls.append(

            Column(controls=[


                Divider(thickness=2),
            #     Vou colocar uma tab aqui para mostrar as semanas
                NewAula()

            ]))



        self.update()







# Estamos alterando para que a tela so cadastre um dia por vez para cada turma
class NewAula(Container):

    def __init__(self, prof_efetivo=None, prof_eventual=None):
        super().__init__()
        self.prof_efetivo=prof_efetivo
        # Drop dos professores
        self.t_drop_prof_eventual=Dropdown(
            width=100)


        # Drop das materias
        self.t_drop_materia=Dropdown(
        width=100)
        self.carragarDropMaterias()


        # Add os elementos no container para aparecer na tela
        self.content=self.t_drop_materia

    def carragarDropMaterias(self):
        for materia in listarMaterias():
            self.t_drop_materia.options.append(dropdown.Option(materia[1]))


    def carregarDropProfessor(self):
        pass








