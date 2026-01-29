from cProfile import label

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Simulate data
    x = np.linspace(0, 7 * np.e, 100)
    print(x)
    y = np.cos(x)

    # Plot cos wave
    plt.plot(x, y, label="cos(x)")
    plt.legend()
    plt.title("COS wave")
    plt.xlabel("x")
    plt.ylabel("COS value")
    # plt.grid(True)
    plt.grid(axis="y")
    plt.show()


if __name__ == "__main__":
    main()
