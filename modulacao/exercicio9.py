from func_compras import adicionar_produto, atualizar_preco, calcular_total

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Produto")
        print("2. Atualizar Preço")
        print("3. Calcular Valor Total")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            atualizar_preco()
        elif escolha == '3':
            total = calcular_total()
            print(f"Valor Total das Compras: R$ {total:.2f}")
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()