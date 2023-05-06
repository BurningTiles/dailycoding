# Solution - 1 May 2023

### [Implement Insertion Sort](https://workat.tech/problem-solving/practice/implement-insertion-sort)

```cpp
void insertionSort(vector<int> &arr) {
	for(int i=1; i<arr.size(); i++) {
		int key = arr[i], j=i-1;
		while(j>=0 && key<arr[j])
			arr[j+1] = arr[j], j--;
		arr[j+1] = key;
	}
}
```

### [Merge Two Sorted Arrays](https://workat.tech/problem-solving/practice/merge-two-sorted-arrays)

```cpp
vector<int> mergeSortedArrays(vector<int> &A, vector<int> &B) {
	vector<int> ans;
	int i=0, j=0;
	while(i<A.size() && j<B.size())
		ans.push_back(A[i]<B[j] ? A[i++] : B[j++]);
	while(i<A.size())
		ans.push_back(A[i++]);
	while(j<B.size())
		ans.push_back(B[j++]);
	return ans;
}
```
