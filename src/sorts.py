# Standard Insertion Sort, scan linearly, find the correct position to insert
#  Find the correct position then shift elements
#  The time complexity is O(n^2) in the average and worst case, 
# and O(n) in the best case (when the array is already sorted).
def insertion_sort(array):
    ar = array.copy() # Work on a copy to avoid modifying the original array
    comparisons = 0 # COMparisons
    shifts = 0 # count the shifts

    for i in range(1, len(a)): # a for loop from the second element to the end
        key = ar[i]
        j = i - 1

        while j >= 0: # scan linearly to find the correct position
            comparisons += 1
            if ar[j] > key:
                ar[j + 1] = ar[j]
                shifts += 1
                j -= 1
            else:
                break

        ar[j + 1] = key # insert the key at the correct position
        shifts += 1

    return ar, comparisons, shifts

# Next we will do binary search on an array, it is called
# binary sort, for the cost breakdown,
# the time complexity is O(n^2) for the worst case and in the best case
# the comparison time complexities is O(n log n) and it is slower than insertion sort
# because of the binary search.

# This is the binary search function to find the correct position to insert
def binary_search(array, key, low, high, counter): # counter is a list to keep track of comparisons
    while low < high: # while low is less than high
        mid = (low + high) // 2 # find the middle index for binary search
        counter[0] += 1 # increment the comparison counter
        if array[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low # return the position to insert

# This is the Binary Insertion Sort function
#  using binary search to find the correct position
def binary_insertion_sort(arr): 
    a = arr.copy() # copy the array to avoid modifying the original
    comparisons = 0
    shifts = 0

#  Loop through each element in the array starting from the second element
    for i in range(1, len(a)):
        key = a[i]

        counter = [0]
        pos = binary_search(a, key, 0, i, counter)
        comparisons += counter[0]

        for j in range(i, pos, -1):
            a[j] = a[j - 1]
            shifts += 1

        a[pos] = key
        shifts += 1

#return the sorted array along with comparison and shift counts
    return a, comparisons, shifts

# Finally we will do improved insertion sort with binary sort elements
def adapted_binary_insertion_sort(arr):
    # Copy the array to avoid modifying the original
    a = arr.copy()
    comparisons = 0 # COMparisons
    shifts = 0 # count the shifts
    last_pos = 0 # Track the last position

    for i in range(1, len(a)): # a for loop from the second element to the end
        key = a[i] # Current element to be inserted

        # See if it is already in order
        comparisons += 1
        if a[i - 1] <= key:
            last_pos = i
            continue

        # Adaptive binary search
        low = last_pos
        high = i

        counter = [0] # Counter for comparisons
        pos = binary_search(a, key, low, high, counter)
        comparisons += counter[0]

        for j in range(i, pos, -1): # Shift elements
            a[j] = a[j - 1]
            shifts += 1
# Insert the key at the correct position
        a[pos] = key
        shifts += 1
        last_pos = pos

    return a, comparisons, shifts


