from flet import *
from DAO.turmaDao import selectTurma

class PainelAula(Container):

    def __init__(self):
        super().__init__()

        self.btnCadastrar=ElevatedButton("Cadastrar", on_click=self.carregarTurmas)
        self.btnAlterar=ElevatedButton("Alterar")
        # Cadastrar
        self.dropPeriodo=Dropdown(
            options=[
                dropdown.Option("Manhã"),
                dropdown.Option("Tarde"),
                dropdown.Option("Noite")
            ]
        )
        self.visible=False
        self.listaTurmas=[]
        self.linha1=Row(controls=[self.btnCadastrar,self.btnAlterar])
        self.listaTurma=Column()
        self.barraTurmas=SearchBar(
        view_elevation=4,
        on_animation_end=self.close,
        divider_color=colors.AMBER,
        bar_hint_text="Escolher a Turma",
        view_hint_text="Escolha a turma para lançar as aulas",

        controls=[
        ListTile(title=ElevatedButton(f"{turma[3]}{turma[4]}", data=turma))
                 for turma in selectTurma()
                 ])

        self.content= Column( controls=[self.linha1,self.barraTurmas])

    def carregarTurmas(self,e):
        pass


    def close(self,e):
        self.barraTurmas.close_view()








