# Solution - 9 May 2023

### [Negative numbers in sorted array](https://workat.tech/problem-solving/practice/negative-numbers-in-sorted-array)

```cpp
int getNegativeNumbersCount(vector<int> &arr) {
	int l=0, r=arr.size()-1, mid, ans = -1;
	while(l<=r) {
		mid = (l+r)/2;
		if(arr[mid]<0) ans = mid, l = mid+1;
		else r = mid-1;
	}
	return ans+1;
}
```

### [Next Greater Element In Sorted Array](https://workat.tech/problem-solving/practice/next-greater-element-in-sorted-array)

```cpp
int getNextGreaterElement(vector<int> &arr, int key) {
	int l=0, r=arr.size()-1, mid, ans = -1;
	while(l<=r) {
		mid = (l+r)/2;
		if(arr[mid] > key) ans = mid, r = mid-1;
		else l = mid+1;
	}
	return ans==-1 ? key : arr[ans];
}
```
