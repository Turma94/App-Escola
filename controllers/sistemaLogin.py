# from flet import *
# from views.viewLogin import *
# from views.viewHome import *
# from views.elements.optionsMenuHide import OptionsMenuHide
# from views.painels.painelProfessor import PainelProfessor
# from views.painels.painelAulas import PainelAula
# from utils.testarEntradasUsuario import *
# # from appMain import  *
#
# telaLogin = ViewLogin()
# # Depois tirar essa função e colocar na controller
# def entrarSistema(e):
#     if validar_email(telaLogin._t_fildlogin.value):
#         telaLogin._t_fildlogin.error_text = ""
#         telaLogin._t_fildlogin.update()
#
#         if testarSenha(telaLogin.t_fild_passWord.value):
#             telaLogin.t_fild_passWord.error_text = ""
#             telaLogin.t_fild_passWord.update()
#
#             # Verificar no banco de dados se o nome e a senha estão la
#
#             page.go("/home")
#         else:
#             telaLogin.t_fild_passWord.error_text = "A senha deve conter 8 caracteres!"
#             telaLogin.t_fild_passWord.update()
#     else:
#         telaLogin._t_fildlogin.error_text = "Digite uma senha com caracteres permitidos"
#         telaLogin._t_fildlogin.update()