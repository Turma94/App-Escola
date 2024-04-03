from flet import *
from DAO.turmaDao import selectTurma
from DAO.professorDAO import selecionarProfessor
from DAO.materiaDAO import listarMaterias
from datetime import datetime
class PainelAulaMatriz(Container):

    def __init__(self, page: Page):
        super().__init__()


        self.meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul',
                      'ago', 'set', 'out', 'nov', 'dez']

        self.title = Text("Cadastrar Aulas", size=38)
        self.btnCadastrar = IconButton(icon=icons.ADD)
        self.status=Checkbox(label="Status")
        self.drop_serie= Dropdown(
            expand=True,
            label="Série",
        )

        self.drop_turma = Dropdown(
            expand=True,
            label="Turma")
        self.carregarTurma()
        self.data = DatePicker(
        # on_change=change_date,
        first_date=datetime(2023, 10, 1),
        last_date=datetime(2024, 10, 1)
        )


        self.page = page
        self.gridAulas=GridView(auto_scroll=True)
        self.coluna_aulas=Column()
        self.gridAulas.controls.append(self.coluna_aulas)


        self.aula=Dropdown(
            width=100,
            label="Aula")
        self.carregarNumeroAula()

        self.p_resp=Dropdown(
            expand=True,
            label="Prof Responsavel")
        self.p_presente=Dropdown(
            expand=True,
            label="Prof Presente")
        self.carregarProfessor()
        self.icon_data=IconButton(icon=icons.DATA_ARRAY)
        self.drop_materia =Dropdown(
            expand=True,
            label="Matéria")
        self.carregarMateria()

        self.content=Column(
            controls=[
                Row(controls=[self.title], alignment=MainAxisAlignment.CENTER),
                Row(controls=
                    [self.drop_turma,self.drop_serie,self.icon_data]),
                Divider(),
                Row(controls=[self.aula,self.p_resp,self.p_presente,self.drop_materia, self.status,self.btnCadastrar])
            ]
        )



    def carregarTurma(self):
        for turma in selectTurma():
            self.drop_turma.options.append(
                dropdown.Option(f"{turma[4]}"),

            )
            self.drop_serie.options.append(
                dropdown.Option(f"{turma[3]}"),
            )



    def carregarNumeroAula(self):

        for aula in (1,2,3,4,5,6,7):
            self.aula.options.append(
                dropdown.Option(str(aula))
            )

    def carregarProfessor(self):

        for prof in selecionarProfessor():
            self.p_resp.options.append(
                dropdown.Option(
                str(f"{prof[1]} {prof[2]}"))
            )
            self.p_presente.options.append(
                dropdown.Option(
                    str(f"{prof[1]} {prof[2]}"))
            )
    def carregarMateria(self):

        for materia in listarMaterias():
            self.drop_materia.options.append(
                dropdown.Option(
                    str(materia[1]))
            )

    # def carregarListaDeAulas(self):
    #
    #     for aula in selecionarAulas():
    #         newAula=AulaModal()
    #         self.coluna_aulas.controls.append(newAula)





class AulaModal(Container):
    def __init__(self,id, id_turma, numero_aula,prof_resp,prof_pres,materia,data,status):
        super().__init__()
        self.btnAlterar = IconButton(icon=icons.MODE)
        self.btnDeletar = IconButton(icon=icons.DELETE_SWEEP)

        self.id = Text(id)

        self.aula = Dropdown(
            width=100,
            label=f"{numero_aula}")
        self.carregarNumeroAula()

        self.p_resp = Dropdown(
            expand=True,
            label=f"{prof_resp}")
        self.p_presente = Dropdown(
            expand=True,
            label=f"{prof_pres}")
        self.carregarProfessor()

        self.drop_materia = Dropdown(
            expand=True,
            label=f"{materia}")
        self.carregarMateria()
        self.status = Checkbox(label="Status")
        self.content = Column(
            controls=[
                Row(controls=[self.aula, self.p_resp, self.p_presente, self.drop_materia, self.status, self.btnAlterar])
            ]
        )


    def carregarNumeroAula(self):
        for aula in (1, 2, 3, 4, 5, 6, 7):
            self.aula.options.append(
                dropdown.Option(str(aula))
            )


    def carregarProfessor(self):
        for prof in selecionarProfessor():
            self.p_resp.options.append(
                dropdown.Option(
                    str(prof[0]))
            )
            self.p_presente.options.append(
                dropdown.Option(
                    str(prof[0]))
            )


    def carregarMateria(self):
        for materia in listarMaterias():
            self.drop_materia.options.append(
                dropdown.Option(
                    str(materia[1]))
            )

