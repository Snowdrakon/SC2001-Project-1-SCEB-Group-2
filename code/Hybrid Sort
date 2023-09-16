#include <stdio.h>

// To execute C, please define "int main()"
void insertion_sort(int arr[], int size, int left){
  for(int i = 1; i < size; i++){
    for(int j = i; j >=0; j--){
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
  int size;
  int threshold;
  scanf("%d", &threshold);
  scanf("%d", &size);
  int array[size];
  for(int i = 0; i < size; i++){
    scanf("%d", &array[i]);
  }
  if(size <= threshold){
    insertion_sort(array, size, 0);
  }
  else{
    hybridSort(array, 0,  size-1, threshold);
  }

  for(int i = 0; i < size; i++){
    printf("%d " , array[i]);
  }
  return 0;
}
