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
                idade = int(linha[len('idade: '):])
            elif linha.startswith('curso: '):
                curso = linha[len('curso: '):]
                if nome_estudante and idade is not None and curso:
                    usuarios[nome_estudante] = {'idade': idade, 'curso': curso}
                    nome_estudante = None
                    idade = None
                    curso = None
    return usuarios

def contagem(usuarios):
    contagem_cursos = {}
    for nome, info in usuarios.items():
        curso = info["curso"]
        if curso in contagem_cursos:
            contagem_cursos[curso] += 1
        else:
            contagem_cursos[curso] = 1
    return contagem_cursos

usuarios = carregar_usuarios()
cont = contagem(usuarios)

for curso, quantidade in cont.items():
    print(f"Curso: {curso}, Estudantes Matriculados: {quantidade}")
