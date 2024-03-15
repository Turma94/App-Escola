from Model.materia import Materia
from Model.usuarios.professor import Professor
from Model.turma import Turma
from Model.aula import Aula
from utils.descobrindo_dia_semana import validar_data
from datetime import date

# Materias
# materia1=Materia("1", "Português")
# materia2=Materia("2", "Matematica")
# materia3=Materia("3", "Inglês")
# materia4=Materia("4", "Física")
#
# #Professor
# professor1=Professor("1","Carlos Silva", "1223", "COMUM","CLT")
# professor2=Professor("2","Maria Aparecida", "1123", "COMUM","CLT")
# professor3=Professor("3","Tereza Rocha", "1233", "COMUM","EVENTUAL")
#

# Atribuições
# professor1.materias.append(materia1)
# professor1.materias.append(materia3)
# professor2.materias.append(materia1)
# professor3.materias.append(materia1)
#
# # Turma
# t_4a=Turma("1","4","A","2024","MANHÃ")
# t_7d=Turma("2","7","D","2024","MANHÃ")
# t_5a=Turma("3","5","A","2024","TARDE")

listaAulas = list()
listaTurmas = list()
listaProf = list()
listaMaterias = list()
idMateria = 1
idProfessor = 1
idTurma = 1
idAula = 1
#Simulando a tela de cadastro de aulas pelo adm
while True:

    print("""
    Sistema Teste
    
    digite 1 para cadastrar Materia
    
    digite 2 para cadastrar professor
    
    digite 3 para cadastrar Turma
    
    digite 4 para cadastrar Aula
    
    digite 5 para gerar relatorios
    
    digite 6 para sair do sistema 
    
    """)

    entrada = input("resposta: ")

    match entrada:
        case "1":
            nome = input("Digite o nome da materia: ")
            materia = Materia(idMateria, nome)
            listaMaterias.append(materia)
            print("materia Cadastrada com sucesso!")
            idMateria += 1

        case "2":
            nomeProf=input("Nome Professor: ")
            senhaProf=input("Digite a sua senha: ")
            nivel="COMUM"
            contrato=input("Esolha o nivel CLT | EVENTUAL | ESTAGIO")
            professor = Professor(idProfessor, nomeProf, senhaProf, nivel, contrato)
            listaProf.append(professor)
            idProfessor+=1
        case "3":
            print("----------Cadastro de Turmas ----------------")
            turma=input("Digite a serie ta turma: ")
            identificador=input("Digite o identificador: ")
            anoLetivo=input("Digite o ano letivo: ")
            periodo=input(" escolha o periodo: MANHÃ | TARDE | NOITE")
            turma=Turma(idTurma, turma, identificador, anoLetivo, "MANHÃ")
            listaTurmas.append(turma)
            idTurma+=1

        case "4":
            print("-----------------Cadastrar Aulas---------------------")
            while True:
                print("Para cadastrar uma aula você necessita escolher  a turma  a materia  e professor ")
                print(" ------------- Lista de Turmas ----------------------- ")
                for turma in listaTurmas:
                    print(turma)

                turmaID=input("digite o id da turma escolhida: ")
                print("#"*50)
                print(" ------------- Lista de Materias ----------------------- ")
                for mat in listaMaterias:
                    print(mat)
                materID = input("digite o id da turma escolhida: ")

                print(" ------------- Lista de Professor ----------------------- ")
                for prof in listaProf:
                    print(prof)
                profId = input("digite o id da turma escolhida: ")


                numeroAula=int(input("Digite a o numero da aula: "))
                while True:
                    print("---------------------Digite a data -----------------------------")
                    ano = int(input("ano: "))
                    mes = int(input("mês: "))
                    dia = int(input("dia: "))
                    dataAula = date(ano, mes, dia)

                    if validar_data(dataAula):
                        listaAulas.append(Aula(idAula, turmaID, profId, materID, numeroAula, dataAula))
                        break
                    else:
                        print("Você precisa digitar uma data valida")
                respostaSairCadastroAula=input("Deseja sair do cadastro de aulas SIM ou NÃO: ")[0].strip().lower()
                if respostaSairCadastroAula == "s":
                    break
        case "5":
            while True:
                print("""
                Digite A: lista de Professores
                Digite B: lista de Materias
                Digite C: lista de Turmas
                Digite D: lista de Aulas
                Digite E: Sair
                """)
                respostaRelatorio=input("Qual relatorio necessita: ")

                match respostaRelatorio:
                    case "A":
                        for prof in listaProf:
                            print(prof)

                    case "B":
                        for materia in listaMaterias:
                            print(materia)

                    case "C":
                        for turmas in listaTurmas:
                            print(turmas)

                    case "C":
                        for aulas in listaAulas:
                            print(aulas)

                    case "E":
                        break

        case "6":
            break


print("finalizou o sistema")