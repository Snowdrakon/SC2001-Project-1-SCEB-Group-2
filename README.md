# Integration of MergeSort and InsertionSort

## Main Idea: 
Set a small integer S as a threshold for the size of subarrays. Once the size of a subarray in a recursive call of Mergesort is less than or equal to S, the algorithm will switch to Insertion Sort, which is efficient for small-sized input.  

## Requirements:
Implement the above algorithm  
Generate Input data(1000 to 10 million), each array has random dataset of integers  
in range [1, ..., x] where x is the largest number  
Analyze time complexity, run program and record key comparisons performed  
Fixing S, plot key comparisons over different sized input  
Fixing input size, plot key comparisons over different values of S  
Using different sizes of input datasets, study how to determine an optimal value of S.  

Compare with original Mergesort: Compare against hybrid algorithm in terms of number of key comparisons and CPU times on dataset with 10 million integers.  

