from flet import *


class PainelMateria(Container):
    def __init__(self):
        super().__init__()
        self.nome_materia=TextField(label="Matéria")
        self.btn_registrar_materia = IconButton(icon=icons.ADD_CIRCLE)
        self.linha=Row(controls=[self.nome_materia,self.btn_registrar_materia], alignment=MainAxisAlignment.CENTER)
        self.offset=transform.Offset(0, 0)
        self.animate_offset=animation.Animation(500)
        self.visible=False

        # Retorna dentro do content
        self.content=self.linha