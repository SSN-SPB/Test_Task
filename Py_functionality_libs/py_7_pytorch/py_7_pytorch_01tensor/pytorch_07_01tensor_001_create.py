import torch


def main():
    # Create tensor 1D
    tensor_1d = torch.tensor([1, -3, 9])
    print(f"Tensor 1D: {tensor_1d}")

    # Create tensor 2D
    tensor_2d = torch.tensor([[1, -3, 9], [1, -3, 9]])
    print(f"Tensor 2D: {tensor_2d}")


if __name__ == "__main__":
    main()
