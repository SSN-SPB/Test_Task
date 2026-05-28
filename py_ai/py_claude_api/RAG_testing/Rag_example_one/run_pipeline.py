from claude_api_request_01_converted import generate_response
from ground_truth import solve_math_problem
from evaluator import evaluate_response


def run(question):
    print("\n====================")
    print("QUESTION:", question)

    # 1. model output
    response = generate_response(question)
    print("\nMODEL RESPONSE:\n", response)

    # 2. ground truth
    gt = solve_math_problem(question)
    print("\nGROUND TRUTH:", gt)

    # 3. evaluation
    evaluation = evaluate_response(question, response, gt)
    print("\nEVALUATION:\n", evaluation)


if __name__ == "__main__":
    question = "How do I solve 5x + 3 = 2 for x?"
    run(question)
