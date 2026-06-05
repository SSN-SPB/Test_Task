from generator import generate_response
from ground_truth import solve_math_problem
from evaluator import evaluate_response


def run(question):
    print("\n====================")
    print("QUESTION:", question)

    response = generate_response(question)
    print("\nMODEL RESPONSE:\n", response)

    gt = solve_math_problem(question)
    print("\nGROUND TRUTH:", gt)

    evaluation = evaluate_response(question, response, gt)
    print("\nEVALUATION:\n", evaluation)


if __name__ == "__main__":
    run("How do I solve 5x + 3 = 2 for x?")
