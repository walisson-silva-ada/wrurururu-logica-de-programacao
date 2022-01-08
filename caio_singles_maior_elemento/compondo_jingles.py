def contagem_compassos(compassos):
    qtd_compassos_corretos = 0
    compassos_incorretos = []
    for compasso in compassos:
        tamanho_compasso = 0
        for i in range(len(compasso)):
            tamanho_compasso = tamanho_compasso + duracao_nota[compasso[i]]
        if tamanho_compasso != 1:
            compassos_incorretos.append(compasso)
        else:
            qtd_compassos_corretos += 1
    print(qtd_compassos_corretos)
    print(compassos_incorretos)

duracao_nota = {'W': 1, 'H': 1 / 2, 'Q': 1 / 4, 'E': 1 / 8, 'S': 1 / 16, 'T': 1 / 32, 'X': 1 / 64}

compassos = input('digite o compassso para verificar se sua duração é correta: ').upper()
compassos = compassos.split('/')
compassos = compassos[1:]
compassos = compassos[:-1]
contagem_compassos(compassos)
