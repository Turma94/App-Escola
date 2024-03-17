from flet import *

class ViewHome(AppBar):

    def __init__(self):
        super().__init__()
        self.btn_menu_hide = IconButton(icon=icons.FORMAT_LIST_BULLETED, icon_color="#ffffff")
        self.leading = self.btn_menu_hide
        self.title = Image(src="logotipoBranco.png")
        self.center_title = True
        self.bgcolor = "#060457"

#teste