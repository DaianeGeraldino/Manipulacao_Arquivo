pesq_nome = input('Digite o nome do usuário: ')

dados_usuarios = []
usuario_atual = {}

with open('usuario.txt', 'r') as arquivo:
    for linha in arquivo:
        chave, valor = linha.strip().split(': ')
        usuario_atual[chave] = valor
        if chave == 'nome' and 'curso' and 'idade':
            dados_usuarios.append(usuario_atual)

print(dados_usuarios)