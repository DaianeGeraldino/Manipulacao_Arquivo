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

def cal_media(usuarios):
    idades = [dados['idade'] for dados in usuarios.values()]
    if idades:
        return sum(idades) / len(idades)
    else:
        return 0

usuarios = carregar_usuarios()
idade_media = cal_media(usuarios)

print(f'A média entre os estudantes é de {idade_media}')
