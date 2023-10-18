import os

def carregar_contatos():
    if os.path.exists('contatos.txt'):
        with open('contatos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            contatos = {}
            for linha in linhas:
                nome, telefone = linha.strip().split(',')
                contatos[nome] = telefone
            return contatos
    else:
        return {}

# Função para salvar os contatos no arquivo
def salvar_contatos(contatos):
    with open('contatos.txt', 'w') as arquivo:
        for nome, telefone in contatos.items():
            arquivo.write(f"{nome},{telefone}\n")

# Função para adicionar um contato
def adicionar_contato(contatos, nome, telefone):
    contatos[nome] = telefone
    salvar_contatos(contatos)

# Função para visualizar todos os contatos
def visualizar_contatos(contatos):
    for nome, telefone in contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

# Função para atualizar um contato
def atualizar_contato(contatos, nome, novo_telefone):
    if nome in contatos:
        contatos[nome] = novo_telefone
        salvar_contatos(contatos)
    else:
        print("Contato não encontrado.")

# Função para excluir um contato
def excluir_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
    else:
        print("Contato não encontrado.")