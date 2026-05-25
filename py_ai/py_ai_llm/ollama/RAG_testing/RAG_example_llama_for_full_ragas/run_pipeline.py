from generator import generate_response
from evaluator import evaluate_response
from ground_truth import solve_math_problem


def run(question):

    print("\n====================")
    print("QUESTION:", question)

    answer, context = generate_response(question)

    print("\nRETRIEVED CONTEXT:")
    print(context)

    gt = solve_math_problem(question)
    print("\nGROUND TRUTH:", gt)

    print("\nMODEL ANSWER:")
    print(answer)

    evaluation = evaluate_response(
        question,
        answer,
        context,
        ground_truth=None
    )

    print("\nEVALUATION:")
    print(evaluation)


if __name__ == "__main__":

    run(
        "What is the project code name?"
    )