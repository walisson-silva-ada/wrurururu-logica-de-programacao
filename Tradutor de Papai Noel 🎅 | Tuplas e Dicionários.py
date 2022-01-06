from test_suite import run_tests
from typing import Tuple, List


def test_case_generator(raw_test_cases: str) -> Tuple[Tuple[str, str], Tuple[str, str]]:
    """
    Build test cases (case, answ) from raw examples provided by the problem

    Example input format accepted:
    | uri-online-judge    | --- NOT FOUND ---    |
    | alemanha      |  Frohliche Weihnachten!    |

    Example output:
    (('uri-online-judge', 'alemanha'), ('--- NOT FOUND ---', 'Frohliche Weihnachten!'))
    """

    # quebra input em linhas, limpa as linhas e remove vazios do inicio e fim para formar um gerador de linhas do input
    lines = (line.split("|")[1:-1] for line in raw_test_cases.splitlines())
    # [[' uri-online-judge    ', ' --- NOT FOUND ---    '], [' alemanha      ', '  Frohliche Weihnachten!    ']]

    # separa as linhas em paises e saudacoes, removendo espacos extras de cada elemento para formar um gerador de lista de tuplas (pais, saudacao):
    cases_answs = (tuple(frase.strip() for frase in line) for line in lines)
    # [('uri-online-judge', '--- NOT FOUND ---'), ('alemanha', 'Frohliche Weihnachten!')]

    # https://stackoverflow.com/a/21911499
    # converte os pares (pais, saudacao) para o formato ((pais, pais), (saudacao, saucao))
    return tuple(zip(*cases_answs))
    # (('uri-online-judge', 'alemanha'), ('--- NOT FOUND ---', 'Frohliche Weihnachten!'))

    # Desempenho?
    # splitlines + n_frases for n_linhas + n_linhas
    # n_linhas   + n_frases  *  n_linhas + n_linhas == n + nf * n + n == n*(nf + 2) == n*nf (O(n))


def build_salutations_dict(raw_salutation_data: str) -> dict[str, str]:
    """
    Generate salutations dict from raw data provided by the problem

    Example input accepted:
    brasil              Feliz Natal!
    alemanha            Frohliche Weihnachten!

    Example output:
    {"brasil": "Feliz Natal!", "alemana": "Frohliche Weihnachten!"}
    """
    # separar o input em linhas e quebrar cada linha por palavra
    data_lines_gen = (d.split() for d in raw_salutation_data.splitlines())
    # formar um dicionario em que a primeira palavra de cada linha é a chave e as demais palabras compõe o valor (unidas em uma única string)
    salutations_dict = {k: " ".join(v) for k, *v in data_lines_gen}

    return salutations_dict


def main():
    ### Getting input data and test cases from files
    input_data = "./papai_noel_input_data"
    test_cases = "./papai_noel_test_cases"
    raw_salutation_data = open(input_data, "r").read()
    raw_test_cases = open(test_cases, "r").read()

    ### building salutations dict
    salutations_dict = build_salutations_dict(raw_salutation_data)

    ### Need this in a function in order to run the tests
    def get_merry_christmas(country):
        return salutations_dict.get(country, "--- NOT FOUND ---")

    ### building test cases and running tests
    cases, answs = test_case_generator(raw_test_cases)
    run_tests(get_merry_christmas, cases, answs)


if __name__ == "__main__":
    main()
