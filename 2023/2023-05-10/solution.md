# Solution - 10 May 2023

### [Insert Position in Sorted Array](https://workat.tech/problem-solving/practice/insert-position-in-sorted-array)

```cpp
int getInsertPosition(vector<int> &arr, int key) {
	int low = 0, high = arr.size()-1;
	while (low <= high) {
		int mid = low + (high-low)/2;
		if (arr[mid] < key) low = mid+1;
		else high = mid-1;
	}
	return low;
}
```
### [LeetCode](https://leetcode.com/problems/search-insert-position/)
```cpp
class Solution {
public:
	int searchInsert(vector<int>& nums, int target) {
		int low = 0, high = nums.size()-1;
		while (low <= high) {
			int mid = low + (high-low)/2;
			if (nums[mid] < target) low = mid+1;
			else high = mid-1;
		}
		return low;
	}
};
```

### [Is Perfect Square](https://workat.tech/problem-solving/practice/is-perfect-square)
### [LeetCode](https://leetcode.com/problems/valid-perfect-square/)
```cpp
bool isPerfectSquare(int num) {
	long long ans = num;
	while(ans*ans > num)
		ans = (ans + num/ans)/2;
	return ans*ans==num;
}
```
