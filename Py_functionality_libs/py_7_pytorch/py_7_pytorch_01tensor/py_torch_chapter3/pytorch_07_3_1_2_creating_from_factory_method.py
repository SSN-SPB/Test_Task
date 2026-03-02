import torch

data_test = [[1, 2], [3, 4]]


def main():
    # Create tensor with 0 value in 3*4 matrix
    tensor_1 = torch.zeros(3, 4)
    print(f"tensor1: {tensor_1}")

    # Output
    # tensor1: tensor([[0., 0., 0., 0.],
    #         [0., 0., 0., 0.],
    #         [0., 0., 0., 0.]])
    # Create tensor with 1 value in 2*2 matrix
    tensor_1_1 = torch.ones(2, 2)
    print(f"tensor1: {tensor_1_1}")
    # tensor1: tensor([[1., 1.],
    #         [1., 1.]])
    # Create tensor with random value between 0 or 1 in 2*20 matrix
    tensor_1_2 = torch.rand(2, 20)
    print(f"tensor1: {tensor_1_2}")
    # Create tensor with normally distributed values in 2*3 matrix
    tensor_1_2 = torch.randn(2, 3)
    print(f"tensor1: {tensor_1_2}")


if __name__ == "__main__":
    main()
