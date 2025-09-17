import ast

source_code = "a + b * 2"

# Parse the code into an AST
tree = ast.parse(source_code, mode="eval")


def main():
    print(ast.dump(tree, indent=4))


if __name__ == "__main__":
    main()

#
# Output:
# Expression(
#     body=BinOp(
#         left=Name(id='a', ctx=Load()),
#         op=Add(),
#         right=BinOp(
#             left=Name(id='b', ctx=Load()),
#             op=Mult(),
#             right=Constant(value=2))))
