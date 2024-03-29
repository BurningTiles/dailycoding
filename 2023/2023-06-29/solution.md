# Solution - 29 Jun 2023

---
## [1. Inversion Count](https://workat.tech/problem-solving/practice/inversion-count) 

### cpp
```cpp
int merge(vector<int> &a, int s, int mid, int e) {
	vector<int> tmp(a.begin() + s, a.begin() + e + 1);
	int count = 0, m = mid-s, i = 0, j = m+1, k = s;
	while(i<=m && j<tmp.size())
		if(tmp[i]<=tmp[j])
			a[k++] = tmp[i++];
		else
			count += m-i+1, a[k++] = tmp[j++];
	while(i<=m) a[k++] = tmp[i++];
	while(j<tmp.size()) a[k++] = tmp[j++];
	return count;
}

int mergeSort(vector<int> &a, int s, int e) {
	int count = 0;
	if(s<e) {
		int mid = s+(e-s)/2;
		count += mergeSort(a, s, mid);
		count += mergeSort(a, mid+1, e);
		count += merge(a, s, mid, e);
	}
	return count;
}

int getInversionCount(vector<int> &array) {
	return mergeSort(array, 0, array.size()-1);
}
```


---
## [2. Search Rotated Sorted Array](https://workat.tech/problem-solving/practice/search-rotated-array) [(LeetCode)](https://leetcode.com/problems/search-in-rotated-sorted-array/) 

### cpp
```cpp
int getElementIndex(vector<int> &array, int target) {
	int left = 0, right = array.size()-1;
	while(left<=right) {
		int mid = left+(right-left)/2;
		if(array[mid]==target) return mid;
		if(array[left]<=array[mid]) {
			if(target>=array[left] && target<array[mid])
				right = mid - 1;
			else
				left = mid + 1;
		} else {
			if(target>array[mid] && target<=array[right])
				left = mid + 1;
			else
				right = mid - 1;
		}
	}
	return -1;
}
```