class Turma:
    def __init__(self, id:int, serie, identificador, anoLetivo, periodo):
        self.__id = id
        self.__serie = serie
        self.__indentficador = identificador
        self.__anoLetivo = anoLetivo
        self.__periodo = periodo
        self.__aulas = []


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

    @property
    def aulas(self):
        return self.__aulas

    def addAula(self, aula):
        if len(self.__aulas) != 0:
            if int(aula.numeroAula) >=1 and int(aula.numeroAula) <=7:
                contemAula = False
                for a in self.__aulas:
                    if aula.numeroAula == a.numeroAula and aula.data == a.data:
                        contemAula = True

                if contemAula == True:
                    print("aula ja existe")

                elif contemAula == False:
                    self.__aulas.append(aula)
                    print("Aula cadastrada com sucesso")
        else:
            if int(aula.numeroAula) >= 1 and int(aula.numeroAula) <= 7:
                self.__aulas.append(aula)
                print("Aula cadastrada com sucesso")

    def verAulas(self):
        for aula in self.__aulas:
            print(f"{aula.idAula} | {aula.idProfessor} | {aula.idMateria} | {aula.numeroAula} | {aula.data} | {aula.status}")



if __name__ == '__main__':

    from Model.aula import Aula

    turma = Turma(5, "5", "C", "2024", "MANHA")

    aula1 = Aula(1, "1-A", "Ze", "Matematica", "2", "10/06/2019")
    aula2 = Aula(1, "1-A", "Ze", "Matematica", "3", "10/06/2019")
    aula3 = Aula(1, "1-A", "Ze", "Matematica", "2", "11/06/2019")
    aula4 = Aula(1, "1-A", "Ze", "Matematica", "3", "10/04/2019")
    aula5 = Aula(1, "1-A", "Ze", "Matematica", "2", "10/06/2019")
    aula6 = Aula(1, "1-A", "Ze", "Matematica", "3", "10/06/2019")
    aula7 = Aula(1, "1-A", "Ze", "Matematica", "5", "12/06/2020")
    aula8 = Aula(1, "1-A", "Ze", "Matematica", "7", "11/01/2019")
    aula9 = Aula(1, "1-A", "Ze", "Matematica", "5", "12/06/2020")


    turma.addAula(aula1)
    turma.addAula(aula2)
    turma.addAula(aula3)
    turma.addAula(aula4)
    turma.addAula(aula5)
    turma.addAula(aula6)
    turma.addAula(aula7)
    turma.addAula(aula8)
    turma.addAula(aula9)

    turma.verAulas()






