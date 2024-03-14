from flet import *

class ViewHome(AppBar):

    def __init__(self):
        super().__init__()
        self.leading=IconButton(icon=icons.FORMAT_LIST_BULLETED,icon_color="#ffffff")
        self.title=Image(src="logotipoBranco.png")
        self.center_title=True
        self.bgcolor = "#060457"