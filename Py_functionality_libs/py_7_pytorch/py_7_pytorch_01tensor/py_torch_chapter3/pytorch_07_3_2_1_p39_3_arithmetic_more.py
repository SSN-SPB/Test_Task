import torch


def main():
    x1 = torch.tensor([1, 2, 3])
    print(f"Square: {torch.pow(x1, 2)}")
    print(f"Square root: {torch.sqrt(x1)}")
    print(f"Exponential: {torch.exp(x1)}")
    print(f"Logarithm: {torch.log(x1)}")
    print(f"Min: {torch.min(x1)}")
    print(f"Max: {torch.max(x1)}")
    print(f"Sum: {torch.sum(x1)}")


if __name__ == "__main__":
    main()
