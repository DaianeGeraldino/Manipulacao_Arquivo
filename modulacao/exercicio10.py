import csv
from func_compras import adicionar_produto, atualizar_preco, calcular_total

def exportar_para_csv(compras, nome_arquivo):
    with open('compras.txt', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Produto', 'Preço'])

        for produto, preco in compras.items():
            escritor.writerow([produto, preco])

def main():
    compras = {}

    while True:
        print("""
Menu:
[1] Adicionar Produto
[2] Atualizar Preço
[3] Calcular Valor Total
[4] Exportar para CSV
[5] Sair
        """)

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: R$"))
            adicionar_produto(compras, produto, preco)
            print(f"Produto '{produto}' adicionado com sucesso.")
        elif escolha == '2':
            produto = input("Digite o nome do produto que deseja atualizar: ")
            novo_preco = float(input("Digite o novo preço: R$"))
            atualizar_preco(compras, produto, novo_preco)
        elif escolha == '3':
            valor_total = calcular_total(compras)
            print(f"Valor total das compras: {valor_total:.2f} reais")
        elif escolha == '4':
            nome_arquivo = input("Digite o nome do arquivo CSV para exportar: ")
            nome_arquivo = f"{nome_arquivo}.csv"
            exportar_para_csv(compras, nome_arquivo)
            print(f"Dicionário de compras exportado para '{nome_arquivo}'")
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()