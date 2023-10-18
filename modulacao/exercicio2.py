from ler_alunos import carregar_alunos

if __name__ == '__main__':
    dados_lidos = {}
    dados_lidos = carregar_alunos()
    for nome, info in dados_lidos.items():
        print(f"Nome: {nome}, Idade: {info['idade']}, Curso: {info['curso']}")
