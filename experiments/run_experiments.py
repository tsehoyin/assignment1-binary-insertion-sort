import random
import time
from src.sorts import (
    insertion_sort, binary_insertion_sort, adapted_binary_insertion_sort
    )

def generate_data(n, case): # Generate different types of array to test time
    if case == "random": # generate random array
        return [random.randint(0, n) for _ in range(n)]
    elif case == "sorted":  # generate an already sorted array
        return list(range(n))
    elif case == "nearly_sorted": # generate a nearly sorted array
        arr = list(range(n))
        # introduce a small disorder by swapping a few elements
        for _ in range(n // 20):
            i = random.randint(0, n - 2)
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr
    else: # unknown case
        raise ValueError("Unknown case")


def run_case(n, case): # Run sorting algorithms on all three cases
    print(f"\nInput case: {case}, n={n}")
    arr = generate_data(n, case)

    for name, func in [ # list of sorting algorithms to test
        ("Insertion Sort", insertion_sort),
        ("Binary Insertion Sort", binary_insertion_sort),
        ("Adapted Binary Insertion Sort", adapted_binary_insertion_sort),
    ]:
        start = time.perf_counter()
        _, comps, shifts = func(arr)
        elapsed = time.perf_counter() - start

        print(f"{name:30} "
              f"Time: {elapsed:.6f}s  "
              f"Comparisons: {comps}  "
              f"Shifts: {shifts}")


if __name__ == "__main__":
    n = 500
    for case in ["random", "sorted", "nearly_sorted"]:
        run_case(n, case)
