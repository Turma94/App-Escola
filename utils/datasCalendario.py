from datetime import datetime, timedelta

# Obtém a data atual
data_atual = datetime.now()

# Define a data inicial (6 meses atrás)
data_inicial = data_atual - timedelta(days=6*30)

# Cria uma lista vazia para armazenar as datas
lista_datas = []

# Loop para adicionar as datas à lista
for i in range(0, 6*30 + 1):
    data = data_inicial + timedelta(days=i)
    lista_datas.append(data)

# Exibe a lista de datas
print(lista_datas)