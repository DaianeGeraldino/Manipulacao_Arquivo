def ler_e_salvar_numeros_em_arquivo(nome_arquivo, n):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for i in range(n):
                numero = int(input(f"Digite o {i+1}º número inteiro: "))
                arquivo.write(str(numero) + '\n')
        print(f"{n} números inteiros foram salvos no arquivo '{nome_arquivo}'.")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")

def calcular_media_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [int(line.strip()) for line in arquivo]
            if numeros:
                media = sum(numeros) / len(numeros)
                print(f"A média dos valores no arquivo '{nome_arquivo}' é: {media:.2f}")
            else:
                print(f"O arquivo '{nome_arquivo}' está vazio.")

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo para salvar os números: ")
    n = int(input("Quantos números inteiros você deseja salvar no arquivo? "))

    ler_e_salvar_numeros_em_arquivo(nome_arquivo, n)
    calcular_media_arquivo(nome_arquivo)
