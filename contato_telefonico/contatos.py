from func_contatos import carregar_contatos, salvar_contatos, adicionar_contato, visualizar_contatos, atualizar_contato, excluir_contato

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
            endereco = input("Digite o endereço do contato: ")
            telefone = input("Digite o telefone do contato: ")
            adicionar_contato(contatos, nome, endereco, telefone)
        elif escolha == '2':
            visualizar_contatos(contatos)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja atualizar: ")
            novo_endereco = input("Digite o novo endereço: ")
            novo_telefone = input("Digite o novo telefone: ")
            atualizar_contato(contatos, nome, novo_endereco, novo_telefone)
        elif escolha == '4':
            nome = input("Digite o nome do contato que deseja excluir: ")
            excluir_contato(contatos, nome)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
