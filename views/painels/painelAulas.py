from flet import *
from DAO.turmaDao import selectTurma

class PainelAula(Container):

    def __init__(self, page:Page):
        super().__init__()
        self.title=Text("Cadastrar Aulas", size=38)
        self.btnCadastrar=ElevatedButton("Cadastrar")
        self.btnAlterar=ElevatedButton("Alterar")
        self.tabelaTurma=GridView(expand=True, max_extent=150, child_aspect_ratio=1)
        self.page=page

        # Configurar o Cadastrar
        self.aulasSemana=BottomSheet(
            content=
                Container(
                    Column(
                        [
                            Row(controls=[]),
                            ElevatedButton("Fechando as aulas Semana", on_click=self.close_aulasSemana),
                        ],
                        tight=True,
                    ),
                    padding=10,
                ),
        open=True,

    )
        self.page.overlay.append(self.aulasSemana)
        self.visible=False

        self.linhaTitutlo=Row(controls=[self.title],alignment=MainAxisAlignment.CENTER)
        self.linha1=Row(controls=[self.btnCadastrar,self.btnAlterar], alignment=MainAxisAlignment.CENTER)
        self.carregarTurmas()
        self.content= Column(controls=[self.linhaTitutlo,self.linha1,self.tabelaTurma])
        self.modalAula=AlertDialog(
                modal=True,
                title=Row(controls=[Text("Aulas"),IconButton(icon=icons.CLOSE, on_click=self.close_modal)],
                          alignment=MainAxisAlignment.SPACE_BETWEEN),
                content=Row(controls=[ElevatedButton("Seg", on_click=self.show_aulasSemana),ElevatedButton("Ter")
                                      ,ElevatedButton("Qua"),ElevatedButton("Qui")
                                      ,ElevatedButton("Sex"),ElevatedButton("Sab")]),
                on_dismiss=lambda e: print("Modal dialog dismissed!"),

            )



    def carregarTurmas(self):
        for turma in selectTurma():
            t=TurmaModal(turma[3],turma[4], self.open_modal)
            self.tabelaTurma.controls.append(
                t
            )

    def pegarTurma(self,serie, sigla):
        return serie,sigla


    def open_modal(self,e):
        print(e.target)
        self.page.dialog = self.modalAula
        self.modalAula.open = True
        self.page.update()


    def close_modal(self,e):
        self.modalAula.open = False
        self.page.update()


    def show_aulasSemana(self,e):
        self.aulasSemana.open = True
        self.aulasSemana.update()

    def close_aulasSemana(self,e):
        self.aulasSemana.open = False
        self.aulasSemana.update()




class TurmaModal(Container):
    def __init__(self,serie,sigla, open_modal):
        super().__init__()
        self.serie=serie
        self.sigla=sigla
        self.content = Column(controls=[
            Text(f"Turma{self.serie}{self.sigla}"),
            IconButton(icon=icons.ADD, on_click=open_modal, data=f"valor{self.serie}{self.sigla}")])
        self.alignment = alignment.center
        self.bgcolor = colors.AMBER_100
        self.border = border.all(1, colors.AMBER_400)
        self.border_radius = border_radius.all(5)






