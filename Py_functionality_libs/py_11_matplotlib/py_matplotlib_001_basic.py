import numpy as np
import matplotlib.pyplot as plt


def main():
    # Create a 1D array (vector)
    x1 = np.linspace(-10,10, 100)
    y1 = x1 * 2
    print(x1, y1)
    plt.plot(x1, y1)
    plt.show()



if __name__ == "__main__":
    main()
