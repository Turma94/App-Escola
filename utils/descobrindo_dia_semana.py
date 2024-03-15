from datetime import date

from holidays.countries import Brazil

DIAS = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

# # primeira forma
# dia_atual = date.today()  # O metodo 'today' retorna o dia atual
#
# indice = dia_atual.weekday()
# # O metodo 'weekday' deve ser usado em um data e retorna um indice para o dia da semana (0-6)
# # e pordemos usar esse indice para lisata de dias 'DIAS'
#
# dia_atual = DIAS[indice]
# print(dia_atual)

# segunda forma
# data = date(day=9, month=3, year=2024)
# indice_da_semana = data.weekday()
# dia_da_semana = DIAS[indice_da_semana]
# print(dia_da_semana)





def validar_data(data):
    # Verifica se a data é um final de semana (sábado ou domingo)
    if data.weekday() >= 5:
        return False

    # Verifica se a data é um feriado no Brasil
    if data in Brazil():
        return False

    return True


if __name__ == '__main__':

    # Exemplo de uso da função
    data_valida = date(2024, 3, 15)  # Quinta-feira
    data_invalida = date(2024, 3, 28)  # sexta santa

    if validar_data(data_valida):
        print("Data válida.")
    else:
        print("Data inválida.")

    if validar_data(data_invalida):
        print("Data válida.")
    else:
        print("Data inválida.")