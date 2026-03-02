# ths available devices for PyTorch tensors
# (torch.tensor([1, 2, 3]).to("device") are:
# "cpu":CPU computation
# "cuda" or "cuda:0": NVIDIA GPU (first GPU)
# "cuda:1", "cuda:2", etc.:Multiple NVIDIA GPUs
# "mps":Apple Silicon GPU (M1/M2/M3)
# "xpu":Intel Arc GPU

import torch


def main():
    x = torch.tensor([1, 2, 3])
    print(f"device before: {x.device}")
    if torch.cuda.is_available():
        x = x.to("cuda")
        print(f"modified device after: {x.device}")


if __name__ == "__main__":
    main()
