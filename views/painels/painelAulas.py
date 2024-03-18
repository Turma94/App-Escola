from flet import *



class PainelAula(UserControl):

    def build(self):
        self.titulo = Text("Gerenciamento de Aulas", size=30)

        self.drop_periodo = Dropdown(label="Período",
                                     options=[
                                       dropdown.Option("Manhã"),
                                       dropdown.Option("Tarde"),
                                       dropdown.Option("Noite")
                                     ])

        self.drop_turma = Dropdown(label="Turma",
                                   options=[
                                       dropdown.Option("1-A"),
                                       dropdown.Option("1-B"),
                                       dropdown.Option("2-A"),
                                       dropdown.Option("2-B")
                                   ])

        self.drop_tipo = Dropdown(label="Tipo",
                                   options=[
                                       dropdown.Option("Semana"),
                                       dropdown.Option("Mês"),
                                       dropdown.Option("Semestre")
                                   ])

        self.list_aulas = Column(alignment=MainAxisAlignment.CENTER)

        return Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Row(controls=[
                Row(controls=[self.drop_periodo, self.drop_turma, self.drop_tipo]),
                FloatingActionButton(icon=icons.CHECK, on_click=self.add_clicked)], alignment=MainAxisAlignment.CENTER),
            self.list_aulas
        ])


    #def add_clicked(self, e):
     #   self.list_aulas.controls.append(Checkbox(label=f"{self.drop_periodo.value} | {self.drop_turma.value} | {self.drop_tipo.value}"))

     #   self.update()

    def add_clicked(self, e):
        self.list_aulas.controls.append(
            Column(controls=[

                Row(controls=[
                    Text("-", size=15)
                ], alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    Dropdown(hint_text="Mês",
                             options=[
                                 dropdown.Option("JANEIRO"),
                                 dropdown.Option("FEVEREIRO"),
                                 dropdown.Option("MARÇO"),
                                 dropdown.Option("ABRIL"),
                                 dropdown.Option("MAIO"),
                                 dropdown.Option("JUNHO"),
                                 dropdown.Option("JULHO"),
                                 dropdown.Option("AGOSTO"),
                                 dropdown.Option("SETEMBRO"),
                                 dropdown.Option("OUTUBRO"),
                                 dropdown.Option("NOVEMBRO"),
                                 dropdown.Option("DEZEMBRO")
                             ], width=200)
                ], alignment=MainAxisAlignment.CENTER),

                Divider(thickness=2),

                Row(controls=[

                    Column(controls=[
                        Row(controls=[IconButton(icon=icons.ARROW_BACK_IOS), IconButton(icon=icons.ARROW_FORWARD_IOS)])
                    ], width=150),

                    Column(controls=[Text("Seg", size=25)], width=150),
                    Column(controls=[Text("Ter", size=25)], width=150),
                    Column(controls=[Text("Qua", size=25)], width=150),
                    Column(controls=[Text("Qui", size=25)], width=150),
                    Column(controls=[Text("Sex", size=25)], width=150),
                    Column(controls=[Text("Sab", size=25)], width=150)

                ], alignment=MainAxisAlignment.CENTER),

                Column(controls=[

                    # Linha 1
                    Row(controls=[
                            # Coluna 1
                            Text("Aula 1", size=25, width=150),

                            # Coluna 2
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),

                            # Coluna 3
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),

                            # Coluna 4
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),

                            # Coluna 5
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),

                            # Coluna 6
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),

                            # Coluna 7
                            Dropdown(options=[
                                dropdown.Option("Maria"),
                                dropdown.Option("Pedro"),
                                dropdown.Option("Carlos"),
                                dropdown.Option("Ana")
                            ], width=150),


                        ], alignment=MainAxisAlignment.CENTER),

                    # Linha 2
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 2", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                    # Linha 3
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 3", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                    # Linha 4
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 4", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                    # Coluna 5
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 5", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                    # Linha 6
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 6", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                    # Linha 7
                    Row(controls=[
                        # Coluna 1
                        Text("Aula 7", size=25, width=150),

                        # Coluna 2
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 3
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 4
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 5
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 6
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                        # Coluna 7
                        Dropdown(options=[
                            dropdown.Option("Maria"),
                            dropdown.Option("Pedro"),
                            dropdown.Option("Carlos"),
                            dropdown.Option("Ana")
                        ], width=150),

                    ], alignment=MainAxisAlignment.CENTER),

                ])

            ])

        )

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









