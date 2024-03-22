from flet import *

class OptionsMenuHide(NavigationDrawer):

    def __init__(self):
        super().__init__()
        # Options
        self.btnHome = NavigationDrawerDestination(
                label="Home",
                icon=icons.HOME,
                selected_icon_content=Icon(icons.HOME_OUTLINED),
            )
        self.btnUsuario = NavigationDrawerDestination(
                label="Usuário",
                icon=icons.VERIFIED_USER_SHARP,
                selected_icon_content=Icon(icons.VERIFIED_USER),
            )
        self.btnProfessores = NavigationDrawerDestination(
                label="Professores",
                icon=icons.PERSON_ADD_ALT_SHARP,
                selected_icon_content=Icon(icons.PERSON_ADD_ALT_OUTLINED),
            )
        self.btnMateria = NavigationDrawerDestination(
                label="Matérias",
                icon=icons.ASSIGNMENT,
                selected_icon_content=Icon(icons.ASSIGNMENT_OUTLINED),
            )
        self.btnAulas = NavigationDrawerDestination(
                label="Aulas",
                icon=icons.CALENDAR_TODAY,
                selected_icon_content=Icon(icons.CALENDAR_TODAY_OUTLINED),
            )
        self.btnRelatorio = NavigationDrawerDestination(
                label="Relatório",
                icon=icons.FOLDER,
                selected_icon_content=Icon(icons.FOLDER_OUTLINED),
            )
        self.btnExit = NavigationDrawerDestination(
                label="Sair",
                icon=icons.EXIT_TO_APP,
                selected_icon_content=Icon(icons.EXIT_TO_APP),
            )

        self.controls = [
            self.btnHome,
            Divider(thickness=2),
            self.btnUsuario,
            Divider(thickness=2),
            self.btnProfessores,
            Divider(thickness=2),
            self.btnMateria,
            Divider(thickness=2),
            self.btnAulas,
            Divider(thickness=2),
            self.btnRelatorio,
            Divider(thickness=2),
            self.btnExit
        ]
