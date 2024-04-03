from flet import *
import re
from DAO.professorDAO import (selecionarProfessor,selecionarProfessor_porID,addProfessor)
from DAO.usuarioDAO import listarUsuario
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
    # def __init__(self):
    #     super.__init__()
    #     self.drop_idUsuario = Dropdown(
    #         expand=True,
    #         label="Usuarios"
    #         )

    def carregarTabela(self):
        for professor in selecionarProfessor():
            self.tabela.rows.append(DataRow(

                cells=[
                    DataCell(Text(professor[0])),
                    DataCell(Text(professor[1])),
                    DataCell(Text(professor[2])),
                    DataCell(Text(professor[3]))
                ], on_select_changed=lambda e: print(f"linha selecionado: {e}"
                                                     )))

    def build(self):


        self.titulo=Text("Professor", size=38)
        # self.idUsuario=TextField(label="Digite o id do usuario")

        # self.carregarIdUSuarios()
        self.t_field_name = TextField(label="Nome")
        self.t_field_sobrenome = TextField(label="Sobrenome",)
        self.drop_contrato=Dropdown(
            label="Contrato",
            hint_text="Escolha um tipo de contrato",
            options=[
                dropdown.Option("EFETIVO"),
                dropdown.Option("EVENTUAL"),
                dropdown.Option("ESTAGIO"),
            ]


        )

        self.list_prof = Column(alignment=MainAxisAlignment.CENTER)

        # application's root control (i.e. "view") containing all other controls


        # A tela que será retornada
        # Colocar aqui a tabela
        # estou criando um espaço para alocar a tabtela
        self.list_view_table_cartridges = GridView(expand=1, spacing=0, padding=0, height=400)

        # estou construindo a tabela
        self.tabela = DataTable(
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("Nome")),
                DataColumn(Text("Sobrenome")),
                DataColumn(Text("Contrato")),

            ],
            expand=True,
            show_checkbox_column=True,
            sort_column_index=0,
            sort_ascending=True,
            on_select_all=True

        )

        # estou chamando a tebela dentro do espaço criado no "Grid" acima
        self.list_view_table_cartridges.controls.append(self.tabela)



        self.carregarTabela()
        return Column(


            controls=[
                Row(controls=[self.titulo], alignment=MainAxisAlignment.CENTER),
                Divider(thickness=2),
                Row(
                    controls=[
                        Row(controls=[self.t_field_name,self.t_field_sobrenome,
                                      self.drop_contrato]),
                        FloatingActionButton(icon=icons.ADD, on_click=self.validar_campos),

                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(controls=[self.list_view_table_cartridges], alignment=MainAxisAlignment.CENTER)
            ]

        )

    # def mostrar_nome_sobrenome(self):
    #     for usuario in selecionarProfessor_porID(1):
    #         self.t_field_name.value=usuario[0]
    #         self.t_field_sobrenome.value = usuario[1]
    #
    #     self.t_field_name.update()
    #     self.t_field_sobrenome.update()

    # def carregarIdUSuarios(self):
    #     for ids in listarUsuario():
    #         self.drop_idUsuario.options.append(ids)

    # def prof_delete(self, professor):
    #     self.list_prof.controls.remove(professor)
    #     self.update()

    def validar_campos(self, e):
        regex_nome = r'^[a-zA-Z\s]+$'
        regex_sobreNome = r'^[a-zA-Z\s]+$'

        validacoes = 0

        if self.t_field_name.value != "":
            if re.match(regex_nome, self.t_field_name.value.replace(" ", "").capitalize()):
                self.t_field_name.error_text = ""
                self.t_field_name.update()
                validacoes += 1
            else:
                self.t_field_name.error_text = "*Nome invalido"
                self.t_field_name.update()
        else:
            self.t_field_name.error_text = "*Campo obrigatorio"
            self.t_field_name.update()

        if self.t_field_sobrenome.value != "":
            if re.match(regex_sobreNome, self.t_field_sobrenome.value.replace(" ", "").capitalize()):
                self.t_field_sobrenome.error_text = ""
                self.t_field_sobrenome.update()
                validacoes += 1
            else:
                self.t_field_sobrenome.error_text = "*SobreNome invalido"
                self.t_field_sobrenome.update()
        else:
            self.t_field_sobrenome.error_text = "*Campo obrigatorio"
            self.t_field_sobrenome.update()

        if self.drop_contrato.value != None:
            self.drop_contrato.error_text = ""
            self.drop_contrato.update()
            validacoes += 1
        else:
            self.drop_contrato.error_text = "*Campo obrigatorio"
            self.drop_contrato.update()

        if validacoes == 3:
            addProfessor(self.t_field_name.value,self.t_field_sobrenome.value,self.drop_contrato.value)




            # self.list_prof.controls.append(Checkbox(
            #     label=f"{self.t_field_name.value.replace(' ', '').capitalize()} | {self.t_field_sobrenome.value.replace(' ', '').capitalize()} | {self.drop_contrato.value}"))
            #
            self.tabela.rows.clear()
            self.carregarTabela()
            self.tabela.update()

            self.t_field_name.value = ""
            self.t_field_sobrenome.value = ""
            self.update()
