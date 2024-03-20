from Model.materia import Materia
from Model.turma import Turma

class Aula:
    def __init__(self, ID_aula, turma:Turma, professorResponsavel, professorPresente, mateia:Materia, numeroAula, data, status=False):

        self.__ID_aula = ID_aula
        self.__turma = turma
        self.__professorResponsavel = professorResponsavel
        self.__professorPresente = professorPresente
        self.__mateia = mateia
        self.__numeroAula = numeroAula
        self.__data = data
        self.__status = status


    @property
    def ID_aula(self):
        return self.__ID_aula

    @property
    def turma(self):
        return self.__turma

    @property
    def professorResponsavel(self):
        return self.__professorResponsavel

    @property
    def professorPresente(self):
        return self.__professorPresente

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
    def setTurma(self, turma):
        self.turma = turma

    @professorResponsavel.setter
    def setProfessorResponsavel(self, professor):
        self.__professor = professor

    @professorPresente.setter
    def setProfessorPresente(self, professor):
        self.professorPresente = professor

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