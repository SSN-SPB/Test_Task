var_a = (
    "a1",
    "a2",
    "a3",
)
var_b = var_a
var_c = (
    "a1",
    "a2",
    "a3",
)
var_set = {var_b, "a7"}

def main():
    print(type(var_set))
    print(var_set)
    # try:
    #     print(var[1])
    # except TypeError as e:
    #     print(f"Set no index: {e}")


if __name__ == "__main__":
    main()
