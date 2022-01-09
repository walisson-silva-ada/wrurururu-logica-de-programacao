def cadastrar_presentes():
    num_pessoas = int(input("Digite o número de pessoas participantes: "))

    cadastro_presentes = {}
    for _ in range(num_pessoas):
        nome = input("Digite um nome: ")
        presentes = [input("Digite um presente: ") for _ in range(3)]
        cadastro_presentes[nome] = presentes

    return cadastro_presentes


def checar_se_acertou_presente(cadastro_presentes, pessoa, presente):
    return presente in cadastro_presentes[pessoa]


def main():
    finalizar = False
    lista_presentes = cadastrar_presentes()
    while not finalizar:
        entrada = input("Digite um nome para checar, ou Q para finalizar o programa")
        if entrada.lower() == "q":
            return

        nome = entrada
        if not (nome in lista_presentes.keys()):
            print("Nome não encontrado, tente outro nome")
            continue

        presente = input("Digite um presente: ")
        acertou = checar_se_acertou_presente(lista_presentes, nome, presente)
        print(
            "Uhul! Seu amigo secreto vai adorar o/" if acertou else "Tente Novamente!"
        )


if __name__ == "__main__":
    main()
