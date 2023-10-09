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
def exibir(usuario):
    print(f'nome: {usuario}')
    print(f'idade: {usuarios[usuario]["Idade"]}')
    print(f'curso: {usuarios[usuario]["Curso"]}')

pesq_nome = input('Digite o nome do usuário: ')
usuarios = carregar_usuarios()

if pesq_nome in usuarios:
    exibir(pesq_nome)
else:
    print('Não encontrado')
