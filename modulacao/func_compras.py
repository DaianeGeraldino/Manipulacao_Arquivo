compras = {}

def adicionar_produto():
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    compras[produto] = preco
    print(f"{produto} foi adicionado à lista de compras.")

def atualizar_preco():
    produto = input("Digite o nome do produto que deseja atualizar: ")
    if produto in compras:
        novo_preco = float(input("Digite o novo preço: "))
        compras[produto] = novo_preco
        print(f"O preço de {produto} foi atualizado para {novo_preco}.")
    else:
        print("Produto não encontrado na lista de compras.")

def calcular_total():
    total = sum(compras.values())
    return total