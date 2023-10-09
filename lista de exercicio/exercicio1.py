dados_usuarios = {
    'nome': '',
    'idade': '',
    'curso': ''
}

usuarios = []

while True:
    # Cria um novo dicionário para cada usuário
    usuario = {}

    nome = input('Insira seu nome: ')
    usuario['nome'] = nome

    idade = int(input('Insira sua idade: '))
    usuario['idade'] = idade

    curso = input('Insira seu curso: ')
    usuario['curso'] = curso

    # Adiciona o dicionário do usuário à lista de usuários
    usuarios.append(usuario)

    confirm = input('Deseja continuar? [Y/N]').lower()
    if confirm != 'y':
        break

print(usuarios)

arquivo_usuario = 'usuarios.txt'

with open(arquivo_usuario, 'w') as arquivo:
    for usuario in usuarios:
        for chave, valor in usuario.items():
            linha = f'{chave}: {valor}\n'
            arquivo.write(linha)
