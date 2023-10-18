def carregar_alunos():
    alunos = {}
    with open('alunos.txt', 'r') as arquivo:
        nome_estudante = None
        idade = None
        curso = None
        for linha in arquivo:
            linha = linha.strip()
            if linha.startswith('nome: '):
                nome_estudante = linha[len('nome: '):]
            elif linha.startswith('idade: '):
                idade = int(linha[len('idade: '):])
            elif linha.startswith('curso: '):
                curso = linha[len('curso: '):]
                if nome_estudante and idade is not None and curso:
                    alunos[nome_estudante] = {'idade': idade, 'curso': curso}
                    nome_estudante = None
                    idade = None
                    curso = None
    return alunos


alunos = carregar_alunos()

def exibir(aluno):
    print(f'nome: {aluno}')
    print(f'idade: {alunos[aluno]["idade"]}')
    print(f'curso: {alunos[aluno]["curso"]}')

