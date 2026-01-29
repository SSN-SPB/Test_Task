import torch
import numpy as np
from numpy.ma.core import equal


def main():
    a2d = np.array([[1, 2], [3, 4]])
    print(f"Initial numpy: {a2d}")
    tensor = torch.from_numpy(a2d)
    print(f"Converted from numpy: {tensor}")
    # Pytorch to Numpy
    back_2_np = tensor.numpy()
    print(f"Restored numpy: {back_2_np}")
    print(back_2_np is a2d)
    print(back_2_np == a2d)



if __name__ == "__main__":
    main()
