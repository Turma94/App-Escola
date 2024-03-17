class Turma:
    def __init__(self, id:int, serie, identificador, anoLetivo, periodo):
        self.__id = id
        self.__serie = serie
        self.__indentficador = identificador
        self.__anoLetivo = anoLetivo
        self.__periodo = periodo
        self.__aulas: list


    @property
    def id(self):
        return self.__id

    @property
    def serie(self):
        return self.__serie

    @property
    def identificador(self):
        return self.__indentficador

    @property
    def anoLetivo(self):
        return self.__anoLetivo

    @property
    def periodo(self):
        return self.__periodo