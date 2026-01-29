import torch


def main():
    s = torch.rand(2, 2)
    print(f"Tensor: {s}")
    print("Using CPU:", torch.cuda.is_available())


if __name__ == "__main__":
    main()
