import ast

source_code = """
def make_sum(a, b):
    result = a + b
    print(result)
    return result
    """

# Parse the code into an AST
tree = ast.parse(source_code)


def main():
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            print(f"Function name: {node.name}")
            print("Arguments:")
            for arg in node.args.args:
                print(f"  - {arg.arg}")
        elif isinstance(node, ast.Return):
            print("Return statement found.")
        elif isinstance(node, ast.Add):
            print("Add statement found.")


if __name__ == "__main__":
    main()
