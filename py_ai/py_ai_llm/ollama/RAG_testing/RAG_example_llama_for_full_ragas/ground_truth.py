import sympy as sp

def solve_math_problem(question: str):
    """
    Simple symbolic ground truth solver for linear equations.
    Designed for evaluation of LLM responses.
    """

    x = sp.Symbol('x')

    # Case 1: 5x + 3 = 2
    if "5x + 3 = 2" in question.replace(" ", ""):
        solution = sp.solve(sp.Eq(5*x + 3, 2), x)
        return str(solution[0])

    # fallback
    return None