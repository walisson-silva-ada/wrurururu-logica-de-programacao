def run_tests(test_func, cases, asnws, nl_after_tests=False):
    for idx, (case, answ) in enumerate(zip(cases, asnws)):
        # tuplefy arguments if they are not tuples already
        case = case if type(case) is tuple else (case,)
        if test_func(*case) == answ:
            print(f"Caso {idx}: Correto ✅ {case} => {test_func(*case)}")
        else:
            print(
                f"""
Caso {idx}: Incorreto ❌
Caso de teste:  {case}
Sua resposta:   {test_func(*case)}
Resposta certa: {answ}"""
            )
        if nl_after_tests:
            print()
