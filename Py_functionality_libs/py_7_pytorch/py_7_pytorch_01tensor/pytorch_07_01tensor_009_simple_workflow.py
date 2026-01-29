import torch


def main():
    # Create tensor
    tensor_1 = torch.arange(0, 10)
    # Reshape tensor
    tensor_1_reshaped = tensor_1.view(2, 5)
    # multiply reshaped
    tensor_1_scaled = tensor_1_reshaped * 2
    tensor_1_scaled_sum = tensor_1_scaled.sum()
    print(f"tensor1: {tensor_1}")
    print(f"tensor reshaped: {tensor_1_reshaped}")
    print(f"tensor multiplied: {tensor_1_scaled}")
    print(f"tensor sum of all elements: {tensor_1_scaled_sum}")


if __name__ == "__main__":
    main()
