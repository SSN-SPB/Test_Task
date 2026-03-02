import torch


def main():

    # values from 0 to 10 with step of 1
    tensor_1 = torch.arange(0, 10, 1)
    # evenly spaced values from 0 to 10 with step of 5
    tensor_2 = torch.linspace(0, 1, steps=5)
    print(f"tensor_1: {tensor_1}")
    print(f"tensor_2: {tensor_2}")


if __name__ == "__main__":
    main()
