from abc import ABC
class User(ABC):
    def __init__(self, id: int, nome: str, senha: str, nivel: str):

        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__nivel = nivel


    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha

    @property
    def nivel(self):
        return self.__nivel


    @nome.setter
    def setNome(self, nome):
        self.__nome = nome

    @senha.setter
    def setSenha(self, senha):
        self.__senha = senha


