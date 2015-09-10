from operator import add, sub, mul, truediv
from sys import maxsize
import re

loglines_active = False
show_ast = True


def log(*logline):
    if loglines_active:
        print("".join(logline))


def eval_basic_expr(expr):
    log("eval_basic_expr_in:          ", expr)

    operand1, operand2 = re.split("[\+\-*/]", expr)
    operation = list(filter(lambda c: True if c == "+" or
                                              c == "-" or
                                              c == "*" or
                                              c == "/" else False, expr))[0]

    operation = {"+": add,
                 "-": sub,
                 "*": mul,
                 "/": truediv}[operation]

    answ = operation(float(operand1), float(operand2))

    log("eval_basic_expr_out:         ", str(answ))
    return answ


def get_priority_operation(expr):
    # ToDo simplify
    log("get_priority_operation_in:   ", expr)

    def get_prec_tier_min(tier_indxs):
        try:
            return min(filter(lambda i: i != -1, tier_indxs))
        except ValueError:
            return maxsize

    mult_index, div_index, add_index, sub_index = map(expr.find, ["*", "/", "+", "-"])

    min_indx_prec1 = get_prec_tier_min([mult_index, div_index])
    min_indx_prec2 = get_prec_tier_min([add_index, sub_index])

    if min_indx_prec1 == maxsize:
        min_indx = min_indx_prec2
    else:
        min_indx = min_indx_prec1

    priority_operation = expr[min_indx]

    log("get_priority_operation_out:  ", priority_operation)
    return priority_operation


def get_priority_scope(expr):
    # ToDo fix
    log("get_priority_scope_in:       ", expr)

    nr_starting_brackets_before_current = 0
    deepest_starting_bracket = 0
    deepest_ending_bracket_index = 0

    for index, symb in enumerate(expr):
        if symb == "(":
            nr_starting_brackets_before_current += 1
        if symb == ")":
            if deepest_starting_bracket < nr_starting_brackets_before_current:
                deepest_starting_bracket = nr_starting_brackets_before_current
                deepest_ending_bracket_index = index
            nr_starting_brackets_before_current = 0

    deepest_starting_bracket_index = expr[:deepest_ending_bracket_index].rfind("(")

    priority_scope = expr[deepest_starting_bracket_index:deepest_ending_bracket_index + 1]

    log("get_priority_scope_out:      ", priority_scope)
    return priority_scope


def get_priority_simple_expr(expr):
    log("get_priority_simple_expr:    ", expr)

    priority_operation = get_priority_operation(expr)
    priority_operation_index = expr.find(priority_operation)

    first_operand = re.split("[\+\-*/()]", expr[:priority_operation_index])[-1]
    second_operand = re.split("[\+\-*/()]", expr[priority_operation_index + 1:])[0]
    operation = expr[priority_operation_index]

    priority_simple_expr = first_operand + operation + second_operand

    log("get_priority_simple_expr:    ", priority_simple_expr)
    return priority_simple_expr


def remove_broken_scope(expr, val):
    # ToDo make obsolete
    return expr.replace("(" + val + ")", val)


def calc_eval(expr, ast=""):
    # ToDo Prettify
    try:
        answ = float(expr)
        if show_ast:
            print()
            print("AST:")
            print(ast + "\n" + expr)
        return answ
    except ValueError:
        pass

    ast += "\n" + expr

    to_eval_expr = get_priority_simple_expr(get_priority_scope(expr))

    to_eval_expr_answer = eval_basic_expr(to_eval_expr)
    new_expr = expr.replace(to_eval_expr, str(to_eval_expr_answer))
    new_expr = remove_broken_scope(new_expr, str(to_eval_expr_answer))

    return calc_eval(new_expr, ast)


if __name__ == "__main__":
    expressions = ["(2+3)",
                   "(2*(2/3)-4)",
                   "(1+1+2-3-3-3)",
                   "(2+2-4*(8-7))",
                   "(1+(2+(3+4))+(5+6)+(7+(8+(9+(10+11))))"]
    for expr in expressions:
        log("Initial expression:          ", expr)
        log("Answer:                      ", str(calc_eval(expr)))
