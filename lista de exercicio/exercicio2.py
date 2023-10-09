arquivo_estudantes = 'usuarios.txt'

dados_lidos = {}
estudante_atual = None

with open(arquivo_estudantes, 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        if linha.startswith('nome: '):
            nome = linha[len('nome: '):]
            estudante_atual = {'nome': nome}
        elif linha.startswith('idade: '):
            idade = int(linha[len('idade: '):])
            estudante_atual['idade'] = idade
        elif linha.startswith('curso: '):
            curso = linha[len('curso: '):]
            estudante_atual['curso'] = curso
            dados_lidos[nome] = estudante_atual

for nome, info in dados_lidos.items():
    print(f"Nome: {nome}, Idade: {info['idade']}, Curso: {info['curso']}")
