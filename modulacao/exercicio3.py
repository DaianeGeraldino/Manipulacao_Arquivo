from ler_alunos import carregar_alunos
from salvar import salvar_alunos

if __name__ == '__main__':
    nome = input("Digite o nome: ")
    alunos = carregar_alunos()

    if nome in alunos:
        print("Estudante encontrado!")
        print("""
        [ 1 ] Idade
        [ 2 ] Curso
        [ 3 ] Sair
        """)
        opcao = input("Digite o que deseja mudar: ")
        if opcao == '1':
            nova_idade = input("Digite a nova idade: ")
            alunos[nome]['idade'] = nova_idade
            salvar_alunos(alunos)
            print("Idade atualizada com sucesso.")
        elif opcao == '2':
            novo_curso = input("Digite o novo curso: ")
            alunos[nome]['curso'] = novo_curso
            salvar_alunos(alunos)
            print(alunos)
            print("Curso atualizado com sucesso.")
        else:
            print("Saindo.")
    else:
        print("Estudante não encontrado!")