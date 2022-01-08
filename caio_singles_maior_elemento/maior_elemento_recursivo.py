lista = [1999, 290, 399, 4999, 2900, 10000, 20, 10, 40002]
def maior_valor(lista, tamanho, indice_maior):
    if tamanho == 0: #se o tamanho for 0 quer dizer que eu ja verifiquei a lista toda
        return lista[indice_maior]
    else:
        if lista[tamanho - 1] > lista[indice_maior]:
            return maior_valor(lista, tamanho - 1, tamanho - 1)
        else:
            return maior_valor(lista, tamanho - 1, indice_maior)


print(maior_valor(lista, len(lista), 0))
