import random

# func. auxiliar para imprimir o(s) vencedor(es), sua(s) pontuação(ões) e cartas
def imprime_vencedores(jogo):
    vencedores = encontra_vencedor(jogo)
    print("vencedores:", vencedores)
    print("-----------------------")
    for nome, jogador in jogo["jogadores"].items():
        print(
            f"{nome:<8}: {jogador['pontos']} pontos   |    {' '.join(jogador['cartas'])}"
        )


# func. auxiliar para cadastrar jogadores
def cadastra_jogadores():
    num_jogadores = int(input("Digite o número de jogadores: "))
    jogadores = {}
    for i in range(num_jogadores):
        nome = input(f"Digite o nome {i+1}º do jogador: ")
        jogadores[nome] = {"nome": nome, "cartas": [], "pontos": 0, "ativo": True}
    return jogadores, num_jogadores


# a) função principal para jogar 21
def jogar_21():
    random.seed(42)
    jogadores, num_jogadores = cadastra_jogadores()

    jogo = {
        "num_jogadores": num_jogadores,
        "num_jogadores_ativos": num_jogadores,
        "jogadores": jogadores,
        "baralho": criar_baralho(),
    }

    while jogo["num_jogadores_ativos"] > 0:
        for nome_jogador in jogo["jogadores"].keys():
            pede_jogada(nome_jogador, jogo)

    imprime_vencedores(jogo)


# b) função para criar um baralho
def criar_baralho():
    naipes = ["♣️", "♥️", "♠️", "♦️"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    baralho = []
    for naipe in naipes:
        for face in faces:
            baralho.append(face + naipe)
    return baralho


# c) função para verificar se jogador está ativo e ver se quer mais uma carta
def pede_jogada(nome_jogador, jogo):
    jogador = jogo["jogadores"][nome_jogador]
    baralho = jogo["baralho"]

    if not jogador["ativo"]:
        return

    comprar = (
        input(
            f"{nome_jogador}, você tem {jogador['pontos']} pontos, deseja comprar mais uma carta? digite 's' se sim, ou qualquer coisa caso contrário"
        ).lower()
        == "s"
    )

    if comprar:
        pontos, carta = comprar_carta(baralho)
        jogador["pontos"] += pontos
        jogador["cartas"].append(carta)
        if jogador["pontos"] >= 21:
            jogador["ativo"] = False
            jogo["num_jogadores_ativos"] -= 1

    else:
        jogador["ativo"] = False
        jogo["num_jogadores_ativos"] -= 1


# d) função para retirar uma carta aleatória do baralho
def comprar_carta(baralho):
    carta = baralho.pop(random.randint(0, len(baralho) - 1))
    face = carta[:-2]

    if face == "A":
        pontos = 1
    elif face == "J" or face == "Q" or face == "K":
        pontos = 10
    else:
        pontos = int(face)

    return pontos, carta


# e) função para encontrar o(s) vencedor(es) da partida
def encontra_vencedor(jogo):
    melhor_pontuacao = -1
    vencedores = []

    for nome, jogador in jogo["jogadores"].items():
        pontos = jogador["pontos"]
        if pontos <= 21:
            if jogador["pontos"] > melhor_pontuacao:
                melhor_pontuacao = jogador["pontos"]
                vencedores = [nome]
            elif jogador["pontos"] == melhor_pontuacao:
                vencedores.append(nome)

    return vencedores


def main():
    jogar_21()


if __name__ == "__main__":
    main()
