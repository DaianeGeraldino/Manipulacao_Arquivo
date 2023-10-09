import os

# Função para carregar os contatos do arquivo
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

# Função principal
def main():
    contatos = carregar_contatos()
    
    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Visualizar Contatos")
        print("3. Atualizar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(contatos, nome, telefone)
        elif escolha == '2':
            visualizar_contatos(contatos)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja atualizar: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contato(contatos, nome, novo_telefone)
        elif escolha == '4':
            nome = input("Digite o nome do contato que deseja excluir: ")
            excluir_contato(contatos, nome)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
