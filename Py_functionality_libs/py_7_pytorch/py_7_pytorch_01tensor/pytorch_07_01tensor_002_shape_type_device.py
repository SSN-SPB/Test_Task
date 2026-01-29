import torch


def main():
    # Create tensor 1D
    tensor_1d = torch.tensor([[1, -3, 9], [3, 3, 1.5]])
    print(f"Tensor 2D: {tensor_1d}")
    print(f"Tensor 2D shape: {tensor_1d.shape}")
    print(f"Tensor 2D type(): {tensor_1d.type()}")
    print(f"Tensor 2D device: {tensor_1d.device}")


# PyTorch can run on different devices:
#
# CPU → "cpu"
#
# GPU (NVIDIA CUDA) → "cuda" or "cuda:0", "cuda:1", etc.
#
# Apple Silicon GPU → "mps" (on macOS)


if __name__ == "__main__":
    main()
