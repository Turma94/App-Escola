from Model.materia import Materia
from Model.turma import Turma

class Aula:
    def __init__(self, aula, turma:Turma, professor, mateia:Materia, numeroAula, data, status=False):

        self.__aula = aula
        self.__turma = turma
        self.__professor = professor
        self.__mateia = mateia
        self.__numeroAula = numeroAula
        self.__data = data
        self.__status = status


    @property
    def aula(self):
        return self.__aula

    @property
    def turma(self):
        return self.__turma

    @property
    def professor(self):
        return self.__professor

    @property
    def materia(self):
        return self.__mateia

    @property
    def numeroAula(self):
        return self.__numeroAula

    @property
    def data(self):
        return self.__data

    @property
    def status(self):
        return self.__status

    @turma.setter
    def setturma(self, turma):
        self.turma = turma

    @professor.setter
    def setprofessor(self, professor):
        self.__professor = professor

    @materia.setter
    def setmateria(self, materia):
        self.__mateia = materia

    @numeroAula.setter
    def setNumeroAula(self, numeroAula):
        self.__numeroAula = numeroAula

    @data.setter
    def setData(self, data):
        self.__data = data

    @status.setter
    def setStatus(self, status):
        self.__status = status









