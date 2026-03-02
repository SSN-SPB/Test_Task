import torch

input_features = 3
output_features = 2


def main():

    # values from 0 to 10 with step of 1
    weight = torch.rand(output_features, input_features)
    print(f"weight: {weight}")
    bias = torch.zeros(output_features)
    print(f"bias: {bias}")


if __name__ == "__main__":
    main()
