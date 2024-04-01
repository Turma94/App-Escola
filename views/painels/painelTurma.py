from flet import *


class PainelTurma(Container):
    def __init__(self):
        super().__init__()
        # Título
        self.titulo = Text("Gerenciamento de Turma", size=30)
        # Subtitulo
        self.subtitulo = Text("NOVA TURMA", size=25, text_align=TextAlign.CENTER)
        # Cadastro
        self.drop_turma = Dropdown(label="Turma", width=300,
                                   options=[
                                       dropdown.Option("1°"), dropdown.Option("2°"),
                                       dropdown.Option("3°"), dropdown.Option("5ª"),
                                       dropdown.Option("6ª"), dropdown.Option("7ª"),
                                       dropdown.Option("8ª"), dropdown.Option("9°")
                                   ])
        self.drop_sigla = Dropdown(label="Sigla", width=300,
                                   options=[
                                       dropdown.Option("A"), dropdown.Option("B"),
                                       dropdown.Option("C"), dropdown.Option("D"),
                                       dropdown.Option("E"), dropdown.Option("F"),
                                       dropdown.Option("G"), dropdown.Option("H")
                                   ])
        self.drop_periodo = Dropdown(label="Periodo", width=300,
                                     options=[
                                         dropdown.Option("Manhã"),
                                         dropdown.Option("Tarde"),
                                         dropdown.Option("Noite")
                                     ])
        self.t_field_ano_letivo = TextField(label="Ano Letivo", width=300)

        self.btn_cadastrar = FilledButton(text="CADASTRAR", width=250, height=50, style=ButtonStyle(bgcolor={
            MaterialState.DEFAULT: "#060457", MaterialState.HOVERED: "#030232"
        }, color="#ffffff", padding=20))
        self.content = Column(controls=[
            Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
            Divider(thickness=2),
            Column(controls=[
                Row(controls=[
                    Container(content=self.subtitulo, border=border.all(2, "#9A9A9A"), width=1010, height=60, margin=40,
                              alignment=alignment.center)],
                    alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.drop_turma, self.drop_sigla], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.t_field_ano_letivo, self.drop_periodo], alignment=MainAxisAlignment.CENTER),
                Row(controls=[self.btn_cadastrar], alignment=MainAxisAlignment.SPACE_AROUND)
            ], alignment=MainAxisAlignment.CENTER)
        ], alignment=MainAxisAlignment.SPACE_AROUND)
        self.offset = transform.Offset(0, 0)
        self.animate_offset = animation.Animation(500)
        self.visible = False

