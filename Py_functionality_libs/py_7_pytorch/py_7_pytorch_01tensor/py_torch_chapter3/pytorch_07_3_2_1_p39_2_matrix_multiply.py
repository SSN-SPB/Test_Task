import torch


def main():
    x1 = torch.tensor([[1.0, 2.0], [12.0, 11.0]])
    x2 = torch.tensor([[3.1, 3.2], [13.1, 13.2]])
    print(f"Matrix multiplication:\n {x1 @ x2}")


if __name__ == "__main__":
    main()
