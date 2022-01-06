from test_suite import run_tests
from typing import Tuple, List


def len_positive_int(n: int):
    """
    Calcula quantos digitos tem um numero inteiro positivo
    """
    l = 1
    while (n := n // 10) != 0:
        l += 1
    return l


def super_digit(n: int):
    """
    Calcula o super digito recursivamente
    """
    if len_positive_int(n) == 1:
        return n

    # ex 9875: super_digit(987) + 5 -> super_digit(98) + 7 + 5 -> super_digit(9) 8 + 7 + 5 -> 9 + 8 + 7 + 5 = 29
    sup = super_digit(n // 10) + n % 10

    # ex 9875: return 29 if 2 == 1 else super_digit(29) -> return super_digit(29)
    return sup if len_positive_int(sup) == 1 else super_digit(sup)


def main():
    def calc_super_digit(n, k):
        # Formando o numero concatenado
        len_n = len_positive_int(n)
        concat_n = n
        for i in range(1, k):
            concat_n += n * 10 ** (len_n * i)

        return super_digit(concat_n)

    cases = [(148, 3), (9875, 4), (123, 3)]

    answs = [
        3,
        8,
        9,
    ]

    run_tests(calc_super_digit, cases, answs)


if __name__ == "__main__":
    main()
