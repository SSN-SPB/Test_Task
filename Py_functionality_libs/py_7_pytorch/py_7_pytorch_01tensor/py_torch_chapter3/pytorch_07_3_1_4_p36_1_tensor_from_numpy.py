import numpy as np
import torch


def main():

    array = np.array([[1, 2], [3, 4]])
    print(f"numpy array: {array}")
    tensor_from_numpy = torch.from_numpy(array)
    print(f"tensor_from_numpy: {tensor_from_numpy}")
    print(f"tensor_from_numpy datatype: {tensor_from_numpy.dtype}")


if __name__ == "__main__":
    main()
