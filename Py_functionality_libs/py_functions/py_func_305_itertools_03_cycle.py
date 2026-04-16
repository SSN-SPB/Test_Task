"""Suit for demo of itertools.cycle
It creates an iterator that returns elements from the iterable
and saves a copy of each. When the iterable is exhausted,
it returns elements from the saved copy, repeating indefinitely."""


from itertools import cycle



list_of_words = ["cat", "dog", "mouse"]



def run_cycle(tested_list):
    cycled_list = cycle(tested_list)
    for _ in range(len(tested_list) * 2):
        print(next(cycled_list))


def main():
    print(run_cycle(list_of_words))


if __name__ == "__main__":
    main()
