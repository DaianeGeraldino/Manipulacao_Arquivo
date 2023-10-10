# Dicionário para armazenar os produtos e seus preços
compras = {}

# Função para adicionar um produto à lista de compras
def adicionar_produto():
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    compras[produto] = preco
    print(f"{produto} foi adicionado à lista de compras.")

# Função para atualizar o preço de um produto
def atualizar_preco():
    produto = input("Digite o nome do produto que deseja atualizar: ")
    if produto in compras:
        novo_preco = float(input("Digite o novo preço: "))
        compras[produto] = novo_preco
        print(f"O preço de {produto} foi atualizado para {novo_preco}.")
    else:
        print("Produto não encontrado na lista de compras.")

# Função para calcular o valor total das compras
def calcular_total():
    total = sum(compras.values())
    return total

# Função principal
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