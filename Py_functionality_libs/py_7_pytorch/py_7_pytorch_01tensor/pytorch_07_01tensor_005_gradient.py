import torch


def main():
    # Create tensor 1D
    tensor_1 = torch.tensor([[1, -3, 9], [3, 3, 1.5]], requires_grad=True)
    tensor_2 = tensor_1 ** 2 + 2 * tensor_1 + 1
    tensor_2.backward(torch.ones_like(tensor_1))
    print(f"tensor1: {tensor_1}")
    print(f"tensor2: {tensor_2}")



if __name__ == "__main__":
    main()
