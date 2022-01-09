from messytester import run_tests
from amigosecreto import main as amigosecreto


def main():
    tests = [
        {
            "test_name": "Amigo secreto",
            "input_simulation": (
                "5",
                "iara",
                "mochila",
                "estojo",
                "lapis",
                "adelar",
                "sapato",
                "camisa",
                "carteira",
                "jessica",
                "agenda",
                "bolsa",
                "brincos",
                "jocelina",
                "xicara",
                "meias",
                "perfume",
                "elaine",
                "sandalia",
                "sapatilha",
                "camiseta",
                "jessica",
                "carteira",
                "jessica",
                "agenda",
                "iara",
                "sandalia",
                "elaine",
                "mochila",
                "iara",
                "mochila",
                "adelar",
                "carteira",
                "Q",
            ),
            "answ": None,
            "expected_prints": "Tente Novamente!\nUhul! Seu amigo secreto vai adorar o/\nTente Novamente!\nTente Novamente!\nUhul! Seu amigo secreto vai adorar o/\nUhul! Seu amigo secreto vai adorar o/\n",
            "verbose": True,
            "run_output_test": False,
            "run_prints_test": True,
        },
    ]

    run_tests(tests, amigosecreto)


if __name__ == "__main__":
    main()
