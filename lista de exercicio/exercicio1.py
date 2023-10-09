dados_usuarios = {
    'nome': '',
    'idade': '',
    'curso': ''
}

usuarios = []


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


print(usuarios)

arquivo_usuario = 'usuarios.txt'

with open(arquivo_usuario, 'a') as arquivo:
    for usuario in usuarios:
        for chave, valor in usuario.items():
            linha = f'{chave}: {valor}\n'
            arquivo.write(linha)
        arquivo.write('\n')
