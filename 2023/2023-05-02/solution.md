# Solution - 2 May 2023

### [Merge Sorted Subarrays](https://workat.tech/problem-solving/practice/merge-sorted-subarrays)

```cpp
void merge(vector<int> &arr, int endIndex) {
	vector<int> sorted;
	int i=0, j=endIndex+1;
	while(i<=endIndex && j<arr.size())
		sorted.push_back(arr[i]<arr[j] ? arr[i++] : arr[j++]);
	while(i<=endIndex)
		sorted.push_back(arr[i++]);
	while(j<arr.size())
		sorted.push_back(arr[j++]);
	for(i=0; i<arr.size(); i++)
		arr[i] = sorted[i];
}
```

### [Implement Merge Sort](https://workat.tech/problem-solving/practice/implement-merge-sort)

```cpp
void merge(vector<int> &arr, int start, int mid, int end) {
	int n = end-start+1, tmp[n], k=0, i=start, j=mid+1;
	while(i<=mid && j<=end)
		tmp[k++] = arr[i]<arr[j] ? arr[i++] : arr[j++];
	while(i<=mid) tmp[k++] = arr[i++];
	while(j<=end) tmp[k++] = arr[j++];
	for(k=0; k<n; k++) arr[start+k] = tmp[k];
}

void mergeSort(vector<int> &arr, int start, int end) {
	if(start<end) {
		int mid = (start + end)/2;
		mergeSort(arr, start, mid);
		mergeSort(arr, mid+1, end);
		merge(arr, start, mid, end);
	}
}

void mergeSort(vector<int> &arr) {
	mergeSort(arr, 0, arr.size()-1);
}
```
