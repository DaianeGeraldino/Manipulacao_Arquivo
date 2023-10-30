import os

def carregar_contatos():
    if os.path.exists('contatos.txt'):
        with open('contatos.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            contatos = {}
            for linha in linhas:
                nome, endereco, telefone = linha.strip().split(',')
                contatos[nome] = {'endereco': endereco, 'telefone': telefone}
            return contatos
    else:
        return {}

def salvar_contatos(contatos):
    with open('contatos.txt', 'w') as arquivo:
        for nome, dados in contatos.items():
            endereco = dados['endereco']
            telefone = dados['telefone']
            arquivo.write(f"{nome},{endereco},{telefone}\n")

def adicionar_contato(contatos, nome, endereco, telefone):
    contatos[nome] = {'endereco': endereco, 'telefone': telefone}
    salvar_contatos(contatos)

def visualizar_contatos(contatos):
    for nome, dados in contatos.items():
        print(f"Nome: {nome}, Endereço: {dados['endereco']}, Telefone: {dados['telefone']}")

def atualizar_contato(contatos, nome, novo_endereco, novo_telefone):
    if nome in contatos:
        contatos[nome]['endereco'] = novo_endereco
        contatos[nome]['telefone'] = novo_telefone
        salvar_contatos(contatos)
    else:
        print("Contato não encontrado.")

def excluir_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
    else:
        print("Contato não encontrado.")
