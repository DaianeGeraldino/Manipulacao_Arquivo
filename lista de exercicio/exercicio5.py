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

def remover_usuario(usuarios, nome_usuario):
    if nome_usuario in usuarios:
        del usuarios[nome_usuario]
        print(f'Estudante {nome_usuario} foi removido')
    else:
        print('Estudante não encontrado')


usuarios = carregar_usuarios()

nome_usuario = input('Digite o nome do usuario ')
remover_usuario(usuarios, nome_usuario)
salvar_usuarios(usuarios)