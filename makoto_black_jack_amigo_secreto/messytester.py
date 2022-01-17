import builtins
import functools
import sys


class Print_buffer:
    def __init__(self):
        self.buffer = ""

    def __repr__(self):
        return self.buffer

    def write(self, string):
        if string[0:5] == "[DBG]":
            return
        self.buffer += string

    def flush_buffer(self):
        self.buffer = ""


original_print = builtins.print
# flushed_print = functools.partial(print, flush=True)
original_input = builtins.input
prints_buffer = Print_buffer()


def testing_input(prompt, test_mode=False, input_simulations=[], verbose=False):
    if not test_mode:
        return original_input(prompt)

    test_input = str(input_simulations.pop(0))
    if verbose:
        original_print("[I]:", prompt, test_input)
    return test_input


def change_input_behavior(test_mode, input_simulations=[], verbose=False):
    builtins.input = functools.partial(
        testing_input,
        test_mode=test_mode,
        input_simulations=input_simulations,
        verbose=verbose,
    )


def testing_print(
    *objects, sep=" ", end="\n", file=sys.stdout, flush=False, verbose=False
):
    string = sep.join(list([str(object) for object in objects])) + end
    if verbose:
        original_print("[P]: ", string, sep="", end="", file=file, flush=True)
    original_print(string, sep="", end="", file=prints_buffer, flush=None)


def chage_print_behavior(test_mode, verbose=False):
    if test_mode:
        builtins.print = functools.partial(testing_print, verbose=verbose)
    else:
        builtins.print = original_print


def run_test(
    test_config,
    test_func_default,
    index=0,
    verbose_default=False,
    run_output_test_default=True,
    run_prints_test_default=False,
):
    pos_inputs = tuplefy(test_config.get("pos_inputs", ()))
    key_inputs = test_config.get("key_inputs", {})
    answ = test_config.get("answ", None)
    input_simulation = tuplefy(test_config.get("input_simulation", ()))
    expected_prints = test_config.get("expected_prints", "")
    index = test_config.get("test_name", index)
    test_func = test_config.get("function", test_func_default)

    verbose = test_config.get("verbose", verbose_default)
    run_output_test = test_config.get("run_output_test", run_output_test_default)
    run_prints_test = test_config.get("run_prints_test", run_prints_test_default)

    # Pega entradas de usuário simuladas como lista pra poder dar pop()
    input_simulation_list = list(input_simulation)
    # Altera o comportamento do print() e input() para realizar teste
    chage_print_behavior(test_mode=True, verbose=verbose)
    change_input_behavior(
        test_mode=True, input_simulations=input_simulation_list, verbose=verbose
    )
    # Apaga o buffer de prints para aferição
    prints_buffer.flush_buffer()  # Isso aqui tá muito feio, usando um global...

    original_print(f"Caso: {index}")

    try:
        test_answ = test_func(*pos_inputs, **key_inputs)

        output_is_correct = test_answ == answ
        print_is_correct = prints_buffer.buffer == expected_prints

        outputs_check = "✔️" if output_is_correct else "❌"
        prints_check = "✔️" if print_is_correct else "❌"

        outputs_check_message = f"outputs: {outputs_check}  " if run_output_test else ""
        prints_check_message = f"prints: {prints_check}  " if run_prints_test else ""
        remaining_user_inputs_warning = (
            f"⚠️☢️ Atenção!!! Sobraram entradas do usuário que não foram usadas: {input_simulation_list}"
            if len(input_simulation_list)
            else ""
        )

        original_print(
            f"{outputs_check_message}{prints_check_message}{remaining_user_inputs_warning}"
        )

        if not (output_is_correct and print_is_correct):

            stripped_print_buffer = prints_buffer.buffer.replace("\n", " | ").rstrip(
                " | "
            )
            stripped_expected_prints = expected_prints.replace("\n", " | ").rstrip(
                " | "
            )

            fn_inputs_line = f"   ➖ Entradas da função:   {pos_inputs}"
            user_inputs_line = f"\n   ➖ Entradas do usuário:  {input_simulation}"
            output_line = (
                f"\n   {outputs_check} Sua resposta:         {test_answ}"
                if run_output_test
                else ""
            )
            expected_output_line = (
                f"\n   ➖ Resposta certa:       {answ}" if run_output_test else ""
            )
            prints_line = (
                f"\n   {prints_check} Prints da função:     {stripped_print_buffer}"
                if run_prints_test
                else ""
            )
            expected_prints_line = (
                f"\n   ➖ Prints corretos:      {stripped_expected_prints}"
                if run_prints_test
                else ""
            )

            original_print(
                f"{fn_inputs_line}{user_inputs_line}{output_line}{expected_output_line}{prints_line}{expected_prints_line}"
            )
    except Exception as inst:
        original_print("⚠️☢️ Erro durante os testes! 💀💀💀")
        original_print(type(inst))  # the exception instance
        original_print(inst.args)  # arguments stored in .args
        original_print(inst)

    original_print("---------------------------------------------------")

    # Recupera o comportamento normal do print() e do input() pois o teste foi finalizado
    change_input_behavior(test_mode=False, input_simulations=[])
    chage_print_behavior(test_mode=False)


def run_tests(
    tests_configs,
    test_func_default,
    verbose_default=False,
    run_output_test_default=True,
    run_prints_test_default=False,
):
    for index, test_config in enumerate(tests_configs):
        run_test(
            test_config,
            test_func_default,
            index,
            verbose_default,
            run_output_test_default,
            run_prints_test_default,
        )


def tuplefy(thing):
    return thing if type(thing) is tuple else (thing,)
