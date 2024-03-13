from Model.materia import Materia
from Model.usuarios.professor import Professor
from Model.turma import Turma
from Model.aula import Aula
from testes.descobrindo_dia_semana import validar_data
from datetime import date

# Materias
materia1=Materia("1", "Português")
materia2=Materia("2", "Matematica")
materia3=Materia("3", "Inglês")
materia4=Materia("4", "Física")

#Professor
professor1=Professor("1","Carlos Silva", "1223", "COMUM","CLT")
professor2=Professor("2","Maria Aparecida", "1123", "COMUM","CLT")
professor3=Professor("3","Tereza Rocha", "1233", "COMUM","EVENTUAL")


# Atribuições
professor1.materias.append(materia1)
professor1.materias.append(materia3)
professor2.materias.append(materia1)
professor3.materias.append(materia1)

# Turma
t_4a=Turma("1","4","A","2024","MANHÃ")
t_7d=Turma("2","7","D","2024","MANHÃ")
t_5a=Turma("3","5","A","2024","TARDE")

listaAulas=list()
#Simulando a tela de cadastro de aulas pelo adm
while True:

    print("""
    Sistema Teste
    
    digite 1 para cadastrar Materia
    
    digite 2 para cadastrar professor
    
    digite 3 para cadastrar Turma
    
    digite 4 para cadastrar Aula
    
    digite 5 para gerar relatorios
    
    """)

    entrada = input("resposta: ")

    match entrada:
        case "1":
            nome = input("Digite o nome da materia: ")
            materia = Materia(None, nome)
            print("materia Cadastrada com sucesso!")

        case "2":



            profrssor = Professor(None)

    ano = int(input("ano: "))
    mes = int(input("mês: "))
    dia = int(input("dia: "))
    dataAula = date(ano, mes, dia)

    if validar_data(dataAula):
        listaAulas.append(Aula("1","1","1","1","1",dataAula))


    else:
        print("Você precisa digitar uma data valida")