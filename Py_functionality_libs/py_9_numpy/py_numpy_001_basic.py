import numpy as np


def main():
    # Create a 1D array (vector)
    a1 = np.array([1, 2, 3])
    print(f"Array a1: {a1}")
    a2 = np.array(3 * np.random.randn(3, 1))
    print(a2)

    # Perform elements multiplying
    b1 = a1 * 2
    print(f"Multyplied array b1: {b1}")

    # Create a 2D array (vector)
    a2d = np.array([[1, 2], [3, 4]])
    print(f"Array a2d: {a2d}")


if __name__ == "__main__":
    main()
