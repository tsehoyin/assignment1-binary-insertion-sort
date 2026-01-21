import random # for generating array
import time # for measuring time complexities
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
              f"Time: {1e9 * elapsed / 100000 :.4f}nanoseconds(shown in class)  "
              f"Comparisons: {comps}  "
              f"Shifts: {shifts}")


if __name__ == "__main__": 

    # Ask user for input size n
    while True:
        try: # input n until valid positive integer is given
            n = int(input("Enter array size n (positive integer): "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    for case in ["random", "sorted", "nearly_sorted"]: #run all cases
        run_case(n, case)
