from ler_alunos import carregar_alunos

if __name__ == '__main__':
    def contagem(alunos):
        contagem_cursos = {}
        for info in alunos.items():
            curso = info["curso"]
            if curso in contagem_cursos:
                contagem_cursos[curso] += 1
            else:
                contagem_cursos[curso] = 1
        return contagem_cursos

    alunos = carregar_alunos()
    cont = contagem(alunos)

    for curso, quantidade in cont.items():
        print(f"Curso: {curso}, Estudantes Matriculados: {quantidade}")
