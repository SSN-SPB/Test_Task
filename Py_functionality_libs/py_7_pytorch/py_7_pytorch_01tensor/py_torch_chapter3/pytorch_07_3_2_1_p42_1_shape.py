import torch


def main():
    x = torch.rand(2, 3)
    print(f"Original tensor: {x}")
    y = torch.rand(3)
    print(y)
    print(f"Tensor to add: {y}")
    matrix_2d = x + y
    print(f"Result's shape: {matrix_2d.shape}")
    print(f"shape of x: {x.shape}")
    print(f"shape of y: {y.shape}")
    print(f"Result's shape: {matrix_2d.shape}")
    print(f"Result of broadcasting addition: {matrix_2d}")


if __name__ == "__main__":
    main()
