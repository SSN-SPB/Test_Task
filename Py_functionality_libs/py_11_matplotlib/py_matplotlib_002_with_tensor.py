import torch
import matplotlib.pyplot as plt


def main():
    # Create 28*28 grayscale image tensor
    image = torch.rand(28, 56)
    # Convert to Numpy for plotting
    selected_color = 'managua'

    plt.imshow(image.numpy(),cmap=selected_color)
    print(f"All possible colors: {plt.colormaps()}")
    # plt.imshow(image.numpy(),cmap='gray')
    plt.title(f"{selected_color}Scale tensor")
    plt.grid("Grid enabled")
    plt.axis("on")
    plt.show()



if __name__ == "__main__":
    main()
