import torch

matrix_2d = torch.tensor([[1, 2, 8], [3, 4, 9]])
vector_1d = torch.tensor([11, 12, 17])

def main():
    result = matrix_2d + vector_1d
    print(f"result of broadcasting: {result}")
    assert result.equal(torch.tensor([[12, 14, 25], [14, 16, 26]]))


if __name__ == "__main__":
    main()
