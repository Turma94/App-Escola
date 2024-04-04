from flet import *
from DAO.turmaDao import selectTurma
from DAO.professorDAO import selecionarProfessor
from DAO.materiaDAO import listarMaterias
from datetime import datetime
from DAO.materiaDAO import selecionarMateria
from DAO.professorDAO import selecionarIDDoProfessor
from DAO.turmaDao import selecionarTurma
from DAO.aulaDAO import addAula
import re

class PainelAulaMatriz(Container):

    def __init__(self, page: Page):
        super().__init__()
        self.visible=False

        self.meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul',
                      'ago', 'set', 'out', 'nov', 'dez']

        self.title = Text("Cadastrar Aulas", size=38)
        self.btnCadastrar = IconButton(icon=icons.ADD, on_click=self.adicionarAula)
        self.status=Checkbox(label="Status")
        self.drop_serie= Dropdown(
            expand=True,
            label="Série",
        )
        self.t_field_data=TextField(label="Data")
        self.drop_turma = Dropdown(
            expand=True,
            label="Turma")
        self.carregarTurma()

        self.data = DatePicker(
        on_change=self.change_date,
        first_date=datetime(2023, 10, 1),
        last_date=datetime(2024, 10, 1),
        date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY
        )


        self.page = page
        self.page.overlay.append(self.data)

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
        self.icon_data=IconButton(icon=icons.CALENDAR_MONTH, on_click=self.abrirCalendario)
        self.drop_materia =Dropdown(
            expand=True,
            label="Matéria")
        self.carregarMateria()

        self.content=Column(
            controls=[
                Row(controls=[self.title], alignment=MainAxisAlignment.CENTER),
                Row(controls=
                    [self.drop_turma,self.drop_serie,self.icon_data,self.t_field_data]),
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

    def abrirCalendario(self,e):
        self.data.pick_date()

    def change_date(self,e):
        valores=self.data.value

        self.t_field_data.value=f"{valores.year}-{valores.month}-{valores.day}"
        self.t_field_data.update()

    def adicionarAula(self, e):
                     # unico padrão aceito 'ano-mes-dia' ex: '2024-04-04'
        regex_1 = r'^\d{4}-\d{2}-\d{2}$'
        regex_2 = r'^\d{4}-\d{1}-\d{2}$'
        regex_3 = r'^\d{4}-\d{2}-\d{1}$'
        regex_4 = r'^\d{4}-\d{1}-\d{1}$'

        totalValidacoes = 0
    ################################################################
        outraValida = 0

        if self.drop_turma.value != None:
            self.drop_turma.error_text = ""
            self.drop_turma.update()
            outraValida += 1
        else:
            self.drop_turma.error_text = "*Campo obrigatorio"
            self.drop_turma.update()

        if self.drop_serie.value != None:
            self.drop_serie.error_text = ""
            self.drop_serie.update()
            outraValida += 1
        else:
            self.drop_serie.error_text = "*Campo obrigatorio"
            self.drop_serie.update()

        if outraValida == 2:

            if len(selecionarTurma(self.drop_serie.value, self.drop_turma.value)) == 1:
                self.drop_serie.error_text = ""
                self.drop_serie.update()
                self.drop_turma.error_text = ""
                self.drop_turma.update()
                totalValidacoes +=1
            else:
                self.drop_serie.error_text = "*A combinação entre turma e serie não existe"
                self.drop_serie.update()
                self.drop_turma.error_text = "*A combinação entre turma e serie não existe"
                self.drop_turma.update()

                     ################################################################
        if self.t_field_data.value != "":

            if re.match(regex_1, self.t_field_data.value) or re.match(regex_2, self.t_field_data.value) or re.match(regex_3, self.t_field_data.value) or re.match(regex_4, self.t_field_data.value):

                semiValidacoes = 0

                if (int(self.t_field_data.value.split("-")[1]) <= 12) and (int(self.t_field_data.value.split("-")[1]) >= 1):
                    self.t_field_data.error_text = ""
                    self.t_field_data.update()
                    semiValidacoes += 1
                else:
                    self.t_field_data.error_text = "*mes invalido"
                    self.t_field_data.update()

                if int(self.t_field_data.value.split("-")[0]) >= int(datetime.today().year):
                    self.t_field_data.error_text = ""
                    self.t_field_data.update()
                    semiValidacoes += 1
                else:
                    self.t_field_data.error_text = f"*Ano não pode ser meno que {datetime.today().year}"
                    self.t_field_data.update()

                if semiValidacoes == 2:
                    self.t_field_data.error_text = ""
                    self.t_field_data.update()
                    totalValidacoes += 1

            else:
                self.t_field_data.error_text = "*Data invalida"
                self.t_field_data.update()
        else:
            self.t_field_data.error_text = "*Campo obrigatorio"
            self.t_field_data.update()

################################################################

        if self.aula.value != None:
            self.aula.error_text = ""
            self.aula.update()
            totalValidacoes += 1
        else:
            self.aula.error_text = "*Campo obrigatorio"
            self.aula.update()

################################################################
        if self.p_resp.value != None:
            self.p_resp.error_text = ""
            self.p_resp.update()
            totalValidacoes += 1
        else:
            self.p_resp.error_text = "*Campo obrigatorio"
            self.p_resp.update()

################################################################

        if self.p_presente.value != None:
            self.p_presente.error_text = ""
            self.p_presente.update()
            totalValidacoes += 1
        else:
            self.p_presente.error_text = "*Campo obrigatorio"
            self.p_presente.update()
################################################################

        if self.drop_materia.value != None:
            self.drop_materia.error_text = ""
            self.drop_materia.update()
            totalValidacoes += 1

        else:
            self.drop_materia.error_text = "*Campo obrigatorio"
            self.drop_materia.update()

        if totalValidacoes == 6:
            id_materia = selecionarMateria(self.drop_materia.value)
            id_prof_resp = selecionarIDDoProfessor(self.p_resp.value.split(" ")[0], self.p_resp.value.split(" ")[1])
            id_prof_presnt = selecionarIDDoProfessor(self.p_presente.value.split(" ")[0], self.p_presente.value.split(" ")[1])
            id_turma = selecionarTurma(self.drop_serie.value, self.drop_turma.value,)

            #addAula(id_turma, id_prof_resp, id_prof_presnt, id_materia, self.t_field_data.value, self.aula.value)


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

