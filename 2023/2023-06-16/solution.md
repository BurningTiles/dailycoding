# Solution - 16 Jun 2023

---
## [1. Find the Missing Number](https://workat.tech/problem-solving/practice/find-the-missing-number) [(LeetCode)](https://leetcode.com/problems/missing-number/) 

```cpp
int findTheMissingNumber(vector<int> &nums) {
	int ans = nums.size()+1;
	for(int i=0; i<nums.size(); i++)
		ans ^= nums[i] ^ (i+1);
	return ans;
}
```

---
## [2. Climbing Stairs](https://workat.tech/problem-solving/practice/climbing-stairs) [(LeetCode)](https://leetcode.com/problems/climbing-stairs/) 

```cpp
int dp[50] = {0, 1, 2};

int climbStairs(int n) {
	if(n<3) return n;
	if(dp[n] != 0) return dp[n];
	return dp[n] = climbStairs(n-1) + climbStairs(n-2);
}
```