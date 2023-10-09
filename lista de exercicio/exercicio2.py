arquivo_usuario = 'usuarios.txt'

dados_lidos = {}

with open(arquivo_usuario, 'r') as arquivo:
    for linha in arquivo:
        chave, valor = linha.strip().split(': ')
        dados_lidos[chave] = valor

print(dados_lidos)