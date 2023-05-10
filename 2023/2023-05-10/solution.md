# Solution - 10 May 2023

### [Insert Position in Sorted Array](https://workat.tech/problem-solving/practice/insert-position-in-sorted-array)

```cpp
int getInsertPosition(vector<int> &arr, int key) {
	if(key>arr.back()) return arr.size();
	int l=0, r=arr.size()-1, mid, ans = -1;
	while(l<=r) {
		mid = (l+r)/2;
		if(arr[mid] >= key) ans = mid, r = mid-1;
		else l = mid+1;
	}
	return ans;
}
```

### [Is Perfect Square](https://workat.tech/problem-solving/practice/is-perfect-square)

```cpp
bool isPerfectSquare(int num) {
	long long ans = num;
	while(ans*ans > num)
		ans = (ans + num/ans)/2;
	return ans*ans==num;
}
```
