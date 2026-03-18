import torch

matrix_2d = torch.tensor([[1, 2, 8], [3, 4, 9]])
# vector_1d = torch.tensor([0.5, 0.5, 0.5])


def main():
    result = matrix_2d.add_(10)
    print(f"Normalized broadcasting via add_: {result}")
    assert result.equal(
        torch.tensor([[11, 12, 18], [13, 14, 19]])
    ), "The result of normalizing is not as expected"


if __name__ == "__main__":
    main()
