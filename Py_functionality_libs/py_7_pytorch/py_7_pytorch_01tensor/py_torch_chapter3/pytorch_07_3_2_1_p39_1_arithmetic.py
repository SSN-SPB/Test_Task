import torch


def main():
    x1 = torch.tensor([1, 2, 3])
    x2 = torch.tensor([3.1, 3.2, 3.3])
    print(f"addition: {x1 + x2}")
    print(f"subtraction: {x1 - x2}")
    print(f"multiplication: {x1 * x2}")
    print(f"division: {x1 / x2}")


if __name__ == "__main__":
    main()
