# Solution - 15 Jun 2023

---
## [1. Count Set Bits](https://workat.tech/problem-solving/practice/count-set-bits) 

```cpp
int countSetBits(int n) {
	int ans = 0;
	while(n)
		ans += n&1, n >>= 1;
	return ans;
}
```

---
## [2. Find the Duplicate Number](https://workat.tech/problem-solving/practice/find-the-duplicate-number) 

```cpp
int findTheDuplicateNumber(vector<int> &nums) {
	int ans = 0;
	for(int i=0; i<nums.size(); i++)
		ans ^= nums[i]^i;
	return ans;
}

/*
// Other solution
int findTheDuplicateNumber(vector<int> &nums) {
	int sum = nums.size() * (nums.size()+1) / 2;
	for(auto &num:nums)
		sum -= num;
	return nums.size() - sum;
}
*/
```