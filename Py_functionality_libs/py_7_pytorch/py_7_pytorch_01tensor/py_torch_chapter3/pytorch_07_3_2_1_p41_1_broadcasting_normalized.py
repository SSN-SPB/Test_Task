import torch

matrix_2d = torch.tensor([[1, 2, 8], [3, 4, 9]])
vector_1d = torch.tensor([0.5, 0.5, 0.5])


def main():
    result = matrix_2d - vector_1d
    print(f"Normalized broadcasting: {result}")
    assert result.equal(
        torch.tensor([[0.5, 1.5, 7.5], [2.5, 3.5, 8.5]])
    ), "The result of broadcasting is not as expected"


if __name__ == "__main__":
    main()
