from Model.materia import Materia
from Model.usuarios.usuario import User
from Model.aula import Aula
from Model.turma import Turma

class Professor(User):
    def __init__(self, id:int, nome: str, senha: str, email:str, nivel: str, contrato: str):
        super().__init__(id, nome, senha, email, nivel)
        self.__contrato = contrato
        self.__materias = []
        self.__aulas = []


    @property
    def contrato(self):
        return self.__contrato

    @property
    def materias(self):
        return self.__materias


    @materias.setter
    def materias(self, materia):
        self.__materias.append(materia)

    @property
    def aulas(self):
        return self.__aulas

    @aulas.setter
    def aulas(self, aula):
        self.__aulas.append(aula)


    #metodos
    def addMateria(self, materia:Materia):
        if type(materia) == Materia:
            self.__materias.append(materia)
        else:
            print("vode pode adicionar materias")

    def addAula(self, aula:Aula):
        if type(aula) != Aula:
            print("nao foi possivel adicionar")
        else:
            self.__aulas.append(aula)
            print("Aula cadastrada com sucesso!")

    def verMaterias(self):
        for materia in self.__materias:
            print(f"ID:{materia.id} | Nome:{materia.nome}")

    def verAulas(self):
        for aula in self.__aulas:
            print(f"`{aula.ID_aula} {aula.turma} {aula.materia} {aula.numeroAula} {aula.data}")

    def addAula(self, entradaAula:Aula):

        hasAula:bool = False

        if len(self.__aulas) != 0:

            if int(entradaAula.numeroAula) >=1 and int(entradaAula.numeroAula) <=7:

                for aulasProfessor in self.__aulas:

                    if (entradaAula.numeroAula == aulasProfessor.numeroAula and entradaAula.data == aulasProfessor.data):

                        hasAula = True

            if hasAula == True:

                print("Já existe uma aula cadastrada!")

            elif hasAula == False:
                self.__aulas.append(entradaAula)

        elif len(self.__aulas) == 0:
            if int(entradaAula.numeroAula) >= 1 and int(entradaAula.numeroAula) <= 7:
                self.__aulas.append(entradaAula)



    def diaAtual(self):
        pass



if __name__ == '__main__':

    materia1 = Materia("1", "Português")
    professor1 = Professor("1", "Carlos Silva", "1223","carlos@gmail.com", "COMUM", "CLT")
    professor2 = Professor("2", "Cristino Ronaldo", "1223", "cri@gmail.com","COMUM", "CLT")
    t_4a = Turma("1", "4", "A", "2024", "MANHÃ")

    ############################################################
    aula1 = Aula(ID_aula="1", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor1.nome, professorPresente=professor1.nome, mateia=materia1.nome, numeroAula="2", data="20/03/2024")
    aula2 = Aula(ID_aula="2", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor2.nome, professorPresente=professor2.nome, mateia=materia1.nome, numeroAula="2", data="20/03/2024")
    aula3 = Aula(ID_aula="3", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor1.nome, professorPresente=professor2.nome, mateia=materia1.nome, numeroAula="2", data="20/04/2024")
    aula4 = Aula(ID_aula="4", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor2.nome, professorPresente=professor1.nome, mateia=materia1.nome, numeroAula="2", data="22/03/2024")
    aula5 = Aula(ID_aula="5", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor1.nome, professorPresente=professor2.nome, mateia=materia1.nome, numeroAula="3", data="20/03/2024")
    aula6 = Aula(ID_aula="6", turma=t_4a.serie + t_4a.identificador, professorResponsavel=professor1.nome, professorPresente=professor1.nome, mateia=materia1.nome, numeroAula="4", data="20/03/2024")

    ###############################################

    professor1.addAula(aula1)
    professor1.addAula(aula2)
    professor1.addAula(aula3)
    professor1.addAula(aula4)
    professor1.addAula(aula5)
    professor1.addAula(aula6)

    professor1.verAulas()


