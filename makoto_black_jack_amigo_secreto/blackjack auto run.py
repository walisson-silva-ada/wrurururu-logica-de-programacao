from messytester import run_tests
from blackjack import jogar_21


def main():
    tests = [
        {
            "test_name": "Black Jack com os dogos",
            "input_simulation": (
                "4",
                "Lobo",
                "Fanny",
                "Apolo",
                "Makoto",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "s",
                "n",
                "s",
                "s",
                "s",
                "s",
                "n",
            ),
            "verbose": True,
            "run_output_test": False,
            "run_prints_test": False,
        },
    ]

    run_tests(tests, jogar_21)


if __name__ == "__main__":
    main()
