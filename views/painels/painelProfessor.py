from flet import *

class NewProfessor(UserControl):
    def __init__(self, name, sobrenome, contrato, delete_prof):
        super().__init__()
        self.name = name
        self.sobrenome = sobrenome
        self.contrato = contrato
        self.delete_prof = delete_prof

    def build(self):
        self.display_prof = Checkbox(value=False, label=f"{self.name} | "
                                                          f"{self.sobrenome} | "
                                                      f"{self.contrato} ")
        self.edit_name = TextField(label="Nome")
        self.edit_sobrenome = TextField(label="Sobrenome", )
        self.edit_drop_contrato = Dropdown(
            label="Contrato",
            hint_text="Escolha um tipo de contrato",
            options=[
                dropdown.Option("CLT"),
                dropdown.Option("EVENTUAL"),
                dropdown.Option("ESTAGIO"),
            ]

        )

        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.display_prof,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Editar",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Deletar",
                            on_click=self.delete_prof,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                self.edit_sobrenome,
                self.edit_drop_contrato,

                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Atualizar",
                    on_click=self.save_clicked,
                ),
            ],
        )
        return Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        self.edit_name.value = str(self.display_prof.label).split(" | ")[0]
        self.edit_sobrenome.value = str(self.display_prof.label).split(" | ")[1]
        self.edit_drop_contrato.value = str(self.display_prof.label).split(" | ")[2]

        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_prof.label = f"{self.edit_name.value} | {self.edit_sobrenome.value} | {self.edit_drop_contrato.value}"
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()


    def delete_clicked(self, e):
        self.delete_prof(self)








class PainelProfessor(UserControl):
    def build(self):
        self.titulo=Text("Professor", size=38)
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
<<<<<<< Updated upstream
        # application's root control (i.e. "view") containing all other controls
=======

        # A tela que será retornada
>>>>>>> Stashed changes
        return Column(

            controls=[
                Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
                Divider(thickness=2),
                Row(
                    controls=[
                        Row(controls=[self.t_field_name, self.t_field_sobrenome, self.drop_contrato]),
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),

                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(controls=[self.list_prof], alignment=MainAxisAlignment.CENTER)
            ]

        )

    def add_clicked(self, e):
        self.list_prof.controls.append(Checkbox(label=f"{self.t_field_name.value} | {self.t_field_sobrenome.value} | {self.drop_contrato.value}"))
        self.t_field_name.value = ""
        self.t_field_sobrenome.value = ""
        self.update()

    def prof_delete(self, professor):
        self.list_prof.controls.remove(professor)
        self.update()