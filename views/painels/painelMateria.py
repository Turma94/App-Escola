from flet import *

class Materia(UserControl):
    def __init__(self, nome, delete_materia):
        super().__init__()
        self.nome = nome
        self.delete_materia = delete_materia

    def delete_clicked(self, e):
        self.delete_materia(self)
    def build(self):
        self.display_materia = Checkbox(value=False, label=self.nome)
        self.editar_materia = TextField()

        self.display_view = Row(
            controls=[
                self.display_materia,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Editar matéria",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Deletar matéria",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ], alignment=MainAxisAlignment.CENTER
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.editar_materia,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Atualizar",
                    on_click=self.save_clicked,
                ),
            ],
        )


        return Column(controls=[self.display_view, self.edit_view], alignment=MainAxisAlignment.CENTER)

    def edit_clicked(self, e):
        self.editar_materia.value = self.display_materia.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_materia.label = self.editar_materia.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()



class PainelMateria(UserControl):
    def build(self):
        self.nova_materia = TextField(hint_text="Matéria")
        self.materias = Column(alignment=MainAxisAlignment.CENTER)

        # application's root control (i.e. "view") containing all other controls
        return Column(

            controls=[
                Row(
                    controls=[
                        self.nova_materia,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],alignment=MainAxisAlignment.CENTER
                ),
                self.materias,
            ], alignment=MainAxisAlignment.CENTER
        )
    def deletar_materia(self, materia):
        self.materias.controls.remove(materia)
        self.update()

    def add_clicked(self, e):
        task = Materia(self.nova_materia.value, self.deletar_materia)
        self.materias.controls.append(task)
        self.nova_materia.value = ""
        self.update()
