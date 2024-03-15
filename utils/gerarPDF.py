from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def salvar_dados_pdf(nome_arquivo, dados):
    # Cria um documento PDF
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Define a fonte e o tamanho do texto
    c.setFont("Helvetica", 12)

    # Escreve os dados no PDF
    for linha in dados:
        c.drawString(100, 700, linha)
        c.translate(0, 20)  # Move para a próxima linha

    # Salva o documento PDF
    c.save()


# Dados para salvar no PDF
dados = [
    "Nome: João da Silva",
    "Idade: 30 anos",
    "Email: exemplo@email.com"
]

# Nome do arquivo PDF a ser criado
nome_arquivo = "dados.pdf"

# Chama a função para salvar os dados no PDF
salvar_dados_pdf(nome_arquivo, dados)

print(f"Dados salvos no arquivo '{nome_arquivo}'.")