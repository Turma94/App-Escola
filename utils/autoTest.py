
from flet import *
from views.viewLogin import ViewLogin
from views.viewHome import ViewHome
from views.elements.optionsMenuHide import OptionsMenuHide
from views.painels.painelProfessor import PainelProfessor
from views.painels.painelAulas import PainelAula
from utils.testarEntradasUsuario import *
import unittest
from faker import Faker
import re
import random

# def validar_email(email):
#     # Expressão regular para validar endereços de e-mail
#     regex_email = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
#
#     # Verifica se o e-mail corresponde à expressão regular
#     if re.match(regex_email, email):
#         return True
#     else:
#         return False


class TestValidarEmail(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_email_valido(self):
        # Testa com e-mails válidos
        for _ in range(100):
            email = self.fake.email()
            print("E-mail Valido",email)
            self.assertTrue(validar_email(email))

    def test_email_invalido(self):
        # Testa com e-mails inválidos
        for _ in range(100):
            primeiroTermo = random.choice([self.fake.word(),"@",".",self.fake.word(),".com"])
            segundoTermo = random.choice([self.fake.word(),"@",".",self.fake.word(),".com"])
            terceitoTermo = random.choice([self.fake.word(),"@",".",self.fake.word(),".com"])
            combincao = f"{primeiroTermo}{segundoTermo}{terceitoTermo}"
            email =  combincao # Gera uma string aleatória não válida como e-mail
            print("E-mail invalido",email)
            self.assertFalse(validar_email(email))


if __name__ == '__main__':
    unittest.main()
