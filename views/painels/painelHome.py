from flet import *



class PainelHome(Container):
    def __init__(self):
        super().__init__()
        self.valorProf=Text()
        self.containerProf=Container(
            width=400,
            bgcolor=colors.CYAN,
            content=Column(
                controls=[
                    Row(controls=[
                        Text("Professor"),
                        Icon(icons.CAST_FOR_EDUCATION_ROUNDED)
                    ]),
                    Row(
                      controls=[
                          self.valorProf
                      ]
                    )
                ]
            )
        )

        self.containerTurmas = Container(
            width=400,
            bgcolor=colors.CYAN,
            content=Column(
                controls=[
                    Row(controls=[
                        Text("Turmas"),
                        Icon(icons.CAST_FOR_EDUCATION_ROUNDED)
                    ]),
                    Row(
                        controls=[
                            self.valorProf
                        ]
                    )
                ]
            )
        )

        self.containerAulas = Container(
            width=400,
            bgcolor=colors.CYAN,
            content=Column(
                controls=[
                    Row(controls=[
                        Text("Aulas ausentes"),
                        Icon(icons.CAST_FOR_EDUCATION_ROUNDED)
                    ]),
                    Row(
                        controls=[
                            self.valorProf
                        ]
                    )
                ]
            )
        )

        self.content = Column(
            controls=[
                Row(controls=[self.containerProf, self.containerTurmas,self.containerAulas])
            ]
        )



class Grafico(Container):
    pass