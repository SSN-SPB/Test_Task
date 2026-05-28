import sympy as sp


def solve_math_problem(question: str):
    """
    Very simple rule-based solver for now.
    You can expand later.
    """

    x = sp.Symbol("x")

    if "5x + 3 = 2" in question:
        expr = sp.Eq(5 * x + 3, 2)
        solution = sp.solve(expr, x)
        return solution  # [-1/5]

    return None
