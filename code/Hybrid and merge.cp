#include <iostream>
#include <cstdlib>
#include <vector>
#include <chrono>
using namespace std;
long long hybridComparisons = 0;
long long mergeSortComparisons = 0;


void merges(vector<int> &arr, int left_arr1, int right_arr1, int left_arr2, int right_arr2){
  vector<int> res; // array store elements after merge
  int pointer1, pointer2;
    pointer1 = left_arr1;
    pointer2 = left_arr2;
  int index = 0;
  while(pointer1 <= right_arr1 && pointer2 <= right_arr2 ){
    if(arr[pointer1] <= arr[pointer2]){
      res.emplace_back(arr[pointer1]);
      pointer1++;
    }
    else{
      res.emplace_back(arr[pointer2]);
      pointer2++;
    }
    index++;
      mergeSortComparisons++;
  }
  if(pointer1 > right_arr1){
    while(pointer2 <= right_arr2){
      res.emplace_back(arr[pointer2]);
      pointer2++;
      index++;
    }
  }
  else{
    while(pointer1 <= right_arr1){
      res.emplace_back(arr[pointer1]);
      pointer1++;
      index++;
    }
  }
  for(int i = left_arr1; i <= right_arr2; i++){
    arr[i] = res[i-left_arr1];
  }
}
void mergesort(vector<int> &arr, int left, int right){
  int mid = (left + right)/2;
  if((right-left) <= 0){
    return;
  }
  else{
    //recursively call to divide the array into subarray
    mergesort(arr, left, mid);
    mergesort(arr, mid+1, right);
  }
  merges(arr, left, mid, mid+1, right);
}
void insertion_sort(vector<int> &arr, int size, int left){
  for(int i = 1; i < size; i++){
    for(int j = i; j > 0; j--){
      if(arr[left + j] < arr[left + j - 1]){
        int temp = arr[left + j - 1];
        arr[left + j - 1] = arr[left + j];
        arr[left + j] = temp;
          hybridComparisons++;
      }
      else{
        break;
      }
    }
  }
}
void merge(vector<int> &arr, int left_arr1, int right_arr1, int left_arr2, int right_arr2){
  vector<int> res ;
  int pointer1, pointer2;
    pointer1 = left_arr1;
    pointer2 = left_arr2;
  int index = 0;
  while(pointer1 <= right_arr1 && pointer2 <= right_arr2 ){
    if(arr[pointer1] <= arr[pointer2]){
      res.emplace_back(arr[pointer1]);
      pointer1++;
    }
    else{
      res.emplace_back(arr[pointer2]);
      pointer2++;
    }
    index++;
      hybridComparisons++;
  }
  if(pointer1 > right_arr1){
    while(pointer2 <= right_arr2){
      res.emplace_back(arr[pointer2]);
      pointer2++;
      index++;
    }
  }
  else{
    while(pointer1 <= right_arr1){
      res.emplace_back(arr[pointer1]);
      pointer1++;
      index++;
    }
  }
  for(int i = left_arr1; i <= right_arr2; i++){
    arr[i] = res[i-left_arr1];
  }
}
void hybridSort(vector<int> &arr, int left, int right, int threshold){
  int mid = (left + right)/2;
  int size = right-left+1;
  if((right-left) <= 0){
    return;
  }
  if(size <= threshold ){
    insertion_sort(arr, size, left);
  }
  else{
    //recursively call to divide the arr into subarr
    hybridSort(arr, left, mid, threshold);
    hybridSort(arr, mid+1, right, threshold);
    merge(arr, left, mid, mid+1, right);
  }
}

int main() {
    srand(time(NULL));
    int size;
    for(int threshold = 30; threshold < 50; threshold++){
        cout <<"Threshold = " << threshold <<" "<<endl;
        for (int i = 1000; i <= 10000000; ) {
                size = i;
                int maxval = 10000000;

                vector<int> arr1, arr2;
                for (int j = 0; j < size; j++) {
                    int r = rand() % maxval;
                    arr1.emplace_back(r);
                    arr2.emplace_back(r);
                }

                // Measure runtime for hybrid sort on arr1
                auto start1 = chrono::high_resolution_clock::now();
                hybridSort(arr1, 0, size - 1, threshold);
                auto end1 = chrono::high_resolution_clock::now();
                auto duration1 = chrono::duration_cast<chrono::microseconds>(end1 - start1).count();
                cout << "For size " << size << ", hybrid sort runtime: " << duration1 << " microseconds" << endl;
                cout << "For size " << size << ", hybrid sort comparisons: " << hybridComparisons << endl;
                hybridComparisons = 0;
            if(i < 1000000){
                i*=10;
            }
            else{
                i += 4000000;
            }

                // Measure runtime for merge sort on arr2
            
                auto start2 = chrono::high_resolution_clock::now();
                mergesort(arr2, 0, size - 1);
                auto end2 = chrono::high_resolution_clock::now();
                auto duration2 = chrono::duration_cast<chrono::microseconds>(end2 - start2).count();
                cout << "For size " << size << ", merge sort runtime: " << duration2 << " microseconds" << endl;
                cout << "For size " << size << ", merge sort comparisons: " << mergeSortComparisons << endl << endl;
                mergeSortComparisons = 0;
             
            }
    }
    
        return 0;
    
}
