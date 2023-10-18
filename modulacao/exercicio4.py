from ler_alunos import carregar_alunos
from ler_alunos import exibir


pesq_nome = input('Digite o nome do usuário: ')
alunos = carregar_alunos()

if pesq_nome in alunos:
    exibir(pesq_nome)
else:
    print('Não encontrado')
