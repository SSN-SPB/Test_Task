import torch


def main():

    # Create tensor with 1 value in 2*2 matrix
    tensor_int = torch.ones(3, dtype=torch.int32)
    tensor_double = torch.zeros(2, 3, dtype=torch.float64)
    print(f"tensor_int datatype: {tensor_int.dtype}")
    print(f"tensor_double datatype: {tensor_double.dtype}")


#     output:
#     "tensor_int datatype: torch.int32"
#     "tensor_double datatype: torch.float64"


if __name__ == "__main__":
    main()
