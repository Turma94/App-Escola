from datetime import datetime, timedelta
from Model.aula import Aula

def obter_data_seguinte(data):
    data_objeto = datetime.strptime(data, '%Y-%m-%d')
    print(data_objeto)

    # Adicionar um dia ao objeto datetime
    data_seguinte = data_objeto + timedelta(days=1)

    print(data_seguinte)
    # Converter o objeto datetime de volta para uma string
    data_seguinte_str = data_seguinte.strftime('%Y-%m-%d')
    print(data_seguinte_str)
    return data_seguinte_str


# data_inicial = '2024-03-31'
# data_proxima = obter_data_seguinte(data_inicial)
# print(f"A data seguinte a {data_inicial} é {data_proxima}")


DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

aulas = []

def cadastrar_aula(aula: Aula, dias_corridos):

    dia_aula = datetime.strptime(aula.data, '%Y-%m-%d')
    nome_dia_semana_inical = dia_aula.weekday()
    nome_dia_semana_atual = DIAS[nome_dia_semana_inical]
    print("este e o dia a ser cadastrado " + nome_dia_semana_atual)
    print("-"*30)

    for i in range(dias_corridos):

        dia_aula = dia_aula + timedelta(days=1)

        nome_dia_semana = dia_aula.weekday()

        nome_dia_semana = DIAS[nome_dia_semana]

        if nome_dia_semana_atual == nome_dia_semana:

            nova_aula = Aula(aula.ID_aula, aula.turma, aula.professorResponsavel, aula.professorPresente, aula.materia, aula.numeroAula, dia_aula)

            aulas.append(nova_aula)

            print(f"Aula cadastrada")

def cadastrar_aula2(aula: list, dias_corridos):

    for i in aula:

        dia_aula = datetime.strptime(i.data, '%Y-%m-%d')
        nome_dia_semana_inical = dia_aula.weekday()
        nome_dia_semana_atual = DIAS[nome_dia_semana_inical]

        for a in range(dias_corridos):

            dia_aula = dia_aula + timedelta(days=1)

            nome_dia_semana = dia_aula.weekday()

            nome_dia_semana = DIAS[nome_dia_semana]

            if nome_dia_semana_atual == nome_dia_semana:

                nova_aula = Aula(i.ID_aula, i.turma, i.professorResponsavel, i.professorPresente, i.materia, i.numeroAula, dia_aula)

                aulas.append(nova_aula)

                print(f"Aula cadastrada")

    print("-"*30)


um_dia_aula = []

aula_1 = Aula("1", "2-A","Carlos","Carlos","Matematica","1","2024-03-11",False)
aula_2 = Aula("2", "2-A","  Ana ","  Ana ","Portugues ","2","2024-03-11",False)
aula_3 = Aula("3", "2-A","  Ana ","  Ana ","Portugues ","3","2024-03-11",False)
aula_4 = Aula("4", "2-A","  Ze  ","  Ze  ","Ed.fisica ","4","2024-03-11",False)
aula_5 = Aula("5", "2-A","  jão ","  Jão "," Historia ","5","2024-03-11",False)
aula_6 = Aula("6", "2-A","  Gui ","  Gui ","Geografia ","6","2024-03-11",False)
aula_7 = Aula("7", "2-A"," Maria"," Maria","   Artes  ","7","2024-03-11",False)

um_dia_aula.append(aula_1)
um_dia_aula.append(aula_2)
um_dia_aula.append(aula_3)
um_dia_aula.append(aula_4)
um_dia_aula.append(aula_5)
um_dia_aula.append(aula_6)
um_dia_aula.append(aula_7)



#cadastrar_aula(aula_1, 30)
cadastrar_aula2(um_dia_aula, 21)

for i in aulas:
    print(f"{i.ID_aula} | {i.turma} | {i.professorResponsavel} | {i.professorPresente} | {i.materia} | {i.numeroAula} | {i.data}")

print(f"total aulas: {len(aulas)}")