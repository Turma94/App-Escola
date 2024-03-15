from flet import *

class PainelProfessor(UserControl):
    def build(self):
        self.titulo=Text("Professor",size=38)
        self.t_field_name = TextField(label="Nome")
        self.t_field_sobrenome = TextField(label="Sobrenome",)
        self.drop_contrato=Dropdown(
            label="Contrato",
            hint_text="Escolha um tipo de contrato",
            options=[
                dropdown.Option("CLT"),
                dropdown.Option("EVENTUAL"),
                dropdown.Option("ESTAGIO"),
            ]

        )

        self.list_prof = Column(alignment=MainAxisAlignment.CENTER)

        # application's root control (i.e. "view") containing all other controls
        return Column(

            controls=[
                Row(controls=[self.titulo],alignment=MainAxisAlignment.CENTER),
                Divider(thickness=2),
                Row(
                    controls=[
                        Row(controls=[self.t_field_name,self.t_field_sobrenome,self.drop_contrato]),
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                self.list_prof,
            ],

        )

    def add_clicked(self, e):
        self.list_prof.controls.append(Checkbox(label=f"{self.t_field_name.value} | {self.t_field_sobrenome.value} | "
                                                      f"{self.drop_contrato.value}"))
        self.t_field_name.value= ""
        self.t_field_sobrenome.value=""
        self.update()