import torch


def main():
    # Create tensor 1D
    tensor_1d = torch.tensor([[1, -3, 9], [3, 3, 1.5]])
    tensor_2d = torch.tensor([[11, -13, 91], [31, 23, 11.5]])
    tensor_sum = tensor_1d + tensor_2d
    print(f"Tensor 1D: {tensor_1d}")
    print(f"Tensor 2D: {tensor_2d}")
    print(f"Tensor sum: {tensor_sum}")
    # Tensor dot
    tensor_1d = torch.tensor([1, -3, 9])
    tensor_2d = torch.tensor([11, -13, 91])
    tensor_dot = torch.dot(tensor_1d, tensor_2d)
    tensor_mult = torch.matmul(tensor_1d, tensor_2d)
    print(f"Tensor dot: {tensor_dot}")
    print(f"Tensor mult: {tensor_mult}")



if __name__ == "__main__":
    main()
