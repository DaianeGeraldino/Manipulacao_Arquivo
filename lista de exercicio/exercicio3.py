pesq_nome = input('Digite o nome do usuário: ')

dados_usuarios = []
usuario_atual = {}

with open('usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        chave, valor = linha.strip().split(': ')
        usuario_atual[chave] = valor
        if chave == 'nome' and 'curso' and 'idade':
            dados_usuarios.append(usuario_atual)

indice_usuario = None
for i, usuario in enumerate(dados_usuarios):
    if 'nome' in usuario and usuario['nome'] == pesq_nome:
        indice_usuario = i
        break

if indice_usuario is not None:

    opcao = input('Deseja alterar o curso ou a idade? ').lower()
    
    if opcao == 'curso':
        
        novo_curso = input('Qual é o novo curso? ')
        dados_usuarios[indice_usuario]['curso'] = novo_curso
        dados_usuarios

    elif opcao == 'idade':
        nova_idade = input('Qual é a nova idade? ')
        dados_usuarios[indice_usuario]['idade'] = nova_idade

    else:
        print('Opção inválida. Por favor, escolha entre "curso" ou "idade".')

    with open('usuarios.txt', 'w') as arquivo:
        for usuario in dados_usuarios:
            for chave, valor in usuario.items():
                arquivo.write(f'{chave}: {valor}\n')

    print(dados_usuarios)
else:
    print('Usuário não encontrado.')
