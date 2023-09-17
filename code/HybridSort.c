#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int comparision = 0;
void insertion_sort(int arr[], int size, int left){
  for(int i = 1; i < size; i++){
    for(int j = i; j > 0; j--){
      if(arr[left + j] < arr[left + j - 1]){
        int temp = arr[left + j - 1];
        arr[left + j - 1] = arr[left + j];
        arr[left + j] = temp;
      }
      else{
        break;
      }
    }
  }
}
void merge(int arr[], int left_arr1, int right_arr1, int left_arr2, int right_arr2){
  int res[right_arr2 - left_arr1 + 1]; // array store elements after merge
  int pointer1, pointer2;
  pointer1 = left_arr1, pointer2 = left_arr2;
  int index = 0;
  while(pointer1 <= right_arr1 && pointer2 <= right_arr2 ){
    if(arr[pointer1] <= arr[pointer2]){
      res[index] = arr[pointer1];
      pointer1++;
    }
    else{
      res[index] = arr[pointer2];
      pointer2++;
    }
    index++;
    comparision++;
  }
  if(pointer1 > right_arr1){
    while(pointer2 <= right_arr2){
      res[index] = arr[pointer2];
      pointer2++;
      index++;
    }
  }
  else{
    while(pointer1 <= right_arr1){
      res[index] = arr[pointer1];
      pointer1++;
      index++;
    }
  }
  for(int i = left_arr1; i <= right_arr2; i++){
    arr[i] = res[i-left_arr1];
  }
}
void hybridSort(int arr[], int left, int right, int threshold){
  int mid = (left + right)/2;
  int size = right-left+1;
  if((right-left) <= 0){
    return;
  }
  if(size <= threshold ){
    insertion_sort(arr, size, left);
  }
  else{
    //recursively call to divide the array into subarray
    hybridSort(arr, left, mid, threshold);
    hybridSort(arr, mid+1, right, threshold);
    merge(arr, left, mid, mid+1, right);
  }
}

int main() {
  srand(time(NULL)); 
  int size;
  for(int i = 1000; i <= 10000000; i *= 10){
    int threshold;
    size = i;
    int array[size];
    int maxval;
    printf("Input the maximum possible value for elements in the array: ");
    scanf("%d", &maxval);
    printf("Input value of threshold: ");
    scanf("%d", &threshold);
    for(int j = 0; j < size; j++){ 
      int r = rand()%maxval; 
      array[j] = r;
    }
    hybridSort(array, 0,  size-1, threshold);
    /*
    for(int i = 0; i < size; i++){
      printf("%d " , array[i]);
    }    
    */
    
    printf("The key comparision is: %d\n", comparision);
    comparision = 0;
  }
  return 0;
}
