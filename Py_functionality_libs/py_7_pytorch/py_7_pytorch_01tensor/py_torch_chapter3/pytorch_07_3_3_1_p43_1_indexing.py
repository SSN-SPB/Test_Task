# This code demonstrates the indexing and broadcasting capabilities of PyTorch tensors.
import torch

tensor_test = torch.tensor([[1, 2, 3], [4, 5, 6], [43, 53, 36]])


def main():
    print(tensor_test)
    print(tensor_test[0])  # First row
    print(tensor_test[1][2])  # Second row and third column
    print(
        tensor_test[2, 2]
    )  # Second row and third column using a different indexing method
    print(tensor_test[:, 0])  # All rows and first column
    print(tensor_test[:, 1])  # All rows and second column
    # First two rows and first two columns
    print(f"First two rows and first two columns {tensor_test[0:2, 0:2]}")
    print(f"Last two rows and last two columns {tensor_test[1:, 1:]}")
    print(tensor_test[0:2, 0:2])  # First two rows and first two columns


if __name__ == "__main__":
    main()
