 Topic 15- adaptive binary/ insertion sort for COMP 359

Overview: 
This project focuses on 
insertion sort, binary sort, 
and the adaptive combination of binary insertion sort. 

The adaptive combination of binary insertion sort is a variant of the insertion sort algorithm,
where the insertion index for each element is found using binary search over the already sorted prefix of the array. 
Also, adaptive optimization is explored that analyzes the positions between insertions to further reduce comparisons. 

Algorithm description:

In insertion sort, 

each new element is inserted into its correct position 
by scanning linearly through the sorted portion of the array.

Analysis framework:

In binary sort, 

Binary sort improves on this by replacing the linear search with binary search, reducing the number of comparisons required to locate the insertion index.

It is faster than insertion sort if the array is not already sorted.
However, it is slower than the insertion sort if the array is already sorted, 
because it still has to do the binary comparisons.


In the adapted binary insertion sort, 

The adapted binary insertion sort improves upon insertion sort by incorporating binary sort elements. It remembers the insertion index and restricting the binary search range accordingly. 

This analyzes locality between consecutive elements, and reducing comparison counts in the sorted data while preserving correctness. 

Time complexities:



In insertion sort,

According to our textbook
Data Structures and Algorithm Analysis Pg225

There are 2 for loops, one for the swapping, and one for the comparison.
The worst case scenario is O(n^2), 
the average case scenario is O(n^2),
the best case scenario, just 1 element array, no comparison, no swappiing
is O(0) (zero)
However, there might be some elements, in the case of an already sorted list, there might be some comparisons, so the Time complexities will be O(n)


In binary sort, 

The comparison, is done with a binary tree search. 
For the number of elements, it is split into 2. The comparison time complexities is O(n log n), because it is log base of 2.
This is faster than insertion sort, in most scenarios, except when the array is already sorted. It is because the comparisons still have to be made, whereas in insertion sort, there is no need for comparisons and shifting. 

The worst case scenario is O(n^2)
The average case scenario is O(n^2),
The best case scenario is O(n log n),



Lastly in our adapted binary insertion sort

We first look if the approximate locations are sorted, then decide if we perform binary search or not. Significantly improving insertion sort, but still retaining some of the benefit of haivng the best case scenario. 


The worst case scenario is O(n^2)
The average case scenario is O(n^2),
The best case scenario is O(0),


Files
sorts.py
run_experiments.py
README.me
