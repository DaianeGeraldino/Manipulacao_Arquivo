dados_alunos = {
    'nome': '',
    'idade': '',
    'curso': ''
}

alunos = []


# Cria um novo dicionário para cada usuário
alunos = {}

nome = input('Insira seu nome: ')
alunos['nome'] = nome

idade = int(input('Insira sua idade: '))
alunos['idade'] = idade

curso = input('Insira seu curso: ')
alunos['curso'] = curso

# Adiciona o dicionário do usuário à lista de usuários
alunos.append(alunos)


print(alunos)

arquivo_alunos = 'alunos.txt'

with open(arquivo_alunos, 'a') as arquivo:
    for alunos in alunos:
        for chave, valor in alunos.items():
            linha = f'{chave}: {valor}\n'
            arquivo.write(linha)
        arquivo.write('\n')
