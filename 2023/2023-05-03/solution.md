# Solution - 3 May 2023

### [Implement Quicksort](https://workat.tech/problem-solving/practice/implement-quicksort)
```cpp
int partition(vector<int> &arr, int left, int right, int pivot) {
	while(left<=right) {
		while(arr[left]<pivot) ++left;
		while(arr[right]>pivot) --right;
		if(left<=right)
			swap(arr[left++], arr[right--]);
	}
	return left;
}

void quickSort(vector<int> &arr, int start, int end) {
	if(start<end) {
		int pivot = arr[(start+end)/2];
		int index = partition(arr, start, end, pivot);
		quickSort(arr, start, index-1);
		quickSort(arr, index, end);
	}
}

void quickSort(vector<int> &arr) {
	quickSort(arr, 0, arr.size()-1);
}
```

### [Square sorted array](https://workat.tech/problem-solving/practice/square-sorted-array)
```cpp
vector<int> getSquareSortedArray(vector<int> &arr) {
    for(auto &a:arr)
		a *= a;
	sort(arr.begin(), arr.end());
	return arr;
}
```