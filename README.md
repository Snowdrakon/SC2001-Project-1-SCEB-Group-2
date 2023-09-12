# Integration of MergerSort and InsertionSort

## Main Idea: 
set a small integer S as a threshold for the size of subarrays. 
Once the size of a subarray in a recursive call of Mergesort is less than or equal to S, 
the algorithm will switch to Insertion Sort, which is efficient for small-sized input.

## Requirements:
Implement the above algorithm
Generate Input data(1000 to 10 million), each array has random dataset of integers
in range [1, ..., x] where x is the largest number
Analyze time complexity, run program and record key comparisons performed
Fixing S, plot key comparisons over different sized input
Fixing input size, 
