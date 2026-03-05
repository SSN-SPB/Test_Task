import torch

data_test = [[1, 2], [3, 4]]


def main():
    # Create tensor
    tensor_1 = torch.tensor(data_test)
    print(f"tensor1: {tensor_1}")


# Output
# tensor1: tensor([[1, 2],
#         [3, 4]])


if __name__ == "__main__":
    main()
