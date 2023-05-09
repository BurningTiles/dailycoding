# Solution - 8 May 2023

### [Contains Element?](https://workat.tech/problem-solving/practice/contains-element)

```cpp
bool containsElement(vector<int> &arr, int key) {
    int l=0, r=arr.size()-1, mid;
	while(l<=r) {
		mid = (l+r)/2;
		if(key<arr[mid]) r = mid-1;
		else if(key>arr[mid]) l = mid+1;
		else return true;
	}
	return false;
}
```

### [Search Range](https://workat.tech/problem-solving/practice/search-range)

```cpp
int find(vector<int> &arr, int key, bool first=true) {
	int l=0, r=arr.size()-1, mid, ans = -1;
	while(l<=r) {
		mid = (l+r)/2;
		if(key < arr[mid]) r = mid-1;
		else if(key>arr[mid]) l = mid+1;
		else ans = mid, first ? r = mid-1 : l = mid+1;
	}
	return ans;
}

vector<int> searchRange(vector<int> &arr, int key) {
    return {find(arr, key), find(arr, key, false)};
}
```
