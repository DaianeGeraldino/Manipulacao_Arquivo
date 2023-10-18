def salvar_alunos(alunos):
    with open('alunos.txt', 'w') as arquivo:
        for nome, dados in alunos.items():
            arquivo.write(f'nome: {nome}\n')
            arquivo.write(f'idade: {dados["idade"]}\n')
            arquivo.write(f'curso: {dados["curso"]}\n')
            arquivo.write('\n')