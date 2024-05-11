# recursion
from time import perf_counter


def print_numbers_recursive(n: int):
    print(n, end=' ')
    if n == 1:
        print("\nDone with recusion!")
        return
    print_numbers_recursive(n - 1)


def print_numbers_loop(n: int):
    while n >= 1:
        print(n, end=' ')
        n -= 1
    print("\nDone with while loop!")



if __name__ == "__main__":
    n = 900
    start1 = perf_counter()
    print_numbers_loop(n)
    end1 = perf_counter()
    print(f"Time taken using loops: {end1 - start1}")

    start2 = perf_counter()
    print_numbers_recursive(n)
    end2 = perf_counter()
    print(f"Time taken using recursion: {end2 - start2}")
