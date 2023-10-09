def carregar_usuarios():
    usuarios = {}
    with open('usuarios.txt', 'r') as arquivo:
        nome_estudante = None
        idade = None
        curso = None
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('nome: '):
                nome_estudante = linha[len('nome: '):]
            elif linha.startswith('idade: '):
                idade = linha[len('idade: '):]
            elif linha.startswith('curso: '):
                curso = linha[len('curso: '):]
                if nome_estudante and idade and curso:
                    usuarios[nome_estudante] = {'Idade': idade, 'Curso': curso}
                    nome_estudante = None
                    idade = None
                    curso = None
    return usuarios

# Função para salvar o dicionário de usuarios de volta no arquivo
def salvar_usuarios(usuarios):
    with open('usuarios.txt', 'w') as arquivo:
        for nome, dados in usuarios.items():
            arquivo.write(f'nome: {nome}\n')
            arquivo.write(f'idade: {dados["Idade"]}\n')
            arquivo.write(f'curso: {dados["Curso"]}\n')
            arquivo.write('\n')

nome = input("Digite o nome: ")
usuarios = carregar_usuarios()

if nome in usuarios:
    print("Estudante encontrado!")
    print("""
    [ 1 ] Idade
    [ 2 ] Curso
    [ 3 ] Sair
    """)
    opcao = input("Digite o que deseja mudar: ")
    if opcao == '1':
        nova_idade = input("Digite a nova idade: ")
        usuarios[nome]['Idade'] = nova_idade
        salvar_usuarios(usuarios)
        print("Idade atualizada com sucesso.")
    elif opcao == '2':
        novo_curso = input("Digite o novo curso: ")
        usuarios[nome]['Curso'] = novo_curso
        salvar_usuarios(usuarios)
        print("Curso atualizado com sucesso.")
    else:
        print("Saindo.")
else:
    print("Estudante não encontrado!")