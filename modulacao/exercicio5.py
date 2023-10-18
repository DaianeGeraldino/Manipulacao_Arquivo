from ler_alunos import carregar_alunos
from salvar import salvar_alunos


if __name__ == '__main__':
    alunos = carregar_alunos()

    def remover_usuario(alunos, nome_usuario):
        if nome_usuario in alunos:
            del alunos[nome_usuario]
            print(f'Estudante {nome_usuario} foi removido')
        else:
            print('Estudante não encontrado')

    alunos = carregar_alunos()

    nome_usuario = input('Digite o nome do usuario ')
    remover_usuario(alunos, nome_usuario)
    salvar_alunos(alunos)