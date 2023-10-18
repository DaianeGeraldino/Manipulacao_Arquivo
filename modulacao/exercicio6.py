from ler_alunos import carregar_alunos


if __name__ == '__main__':
    def cal_media(alunos):
        idades = [dados['idade'] for dados in alunos.values()]
        if idades:
            return sum(idades) / len(idades)
        else:
            return 0

    alunos = carregar_alunos()
    idade_media = cal_media(alunos)

    print(f'A média entre os estudantes é de {idade_media}')
