import torch


def main():

    # values from 0 to 10 with step of 1
    tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])

    print(f"tensor_1 dimension : {tensor_1.ndim}")
    print(f"tensor_1 shape : {tensor_1.shape}")


if __name__ == "__main__":
    main()
