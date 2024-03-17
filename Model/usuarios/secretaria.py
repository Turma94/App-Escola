from Model.usuarios.usuario import User
class Secretaria(User):
    def __init__(self, id: str, nome: str, senha: str, nivel: str):
        super().__init__(id, nome, senha, nivel)