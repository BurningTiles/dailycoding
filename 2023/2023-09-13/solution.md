# Solution - 13 Sep 2023

---
## [1. Power Set](https://workat.tech/problem-solving/practice/power-set) [(LeetCode)](https://leetcode.com/problems/subsets/) 

### cpp
```cpp
vector<vector<int>> getPowerSet(vector<int> &nums) {
	vector<vector<int>> subsets;
	for(int i=0; i<1L<<nums.size(); i++){
		long long x = i;
		vector<int> subset;
		for(int j=0; j<11 && x; j++, x/=2)
			if(x&1) subset.push_back(nums[j]);
		subsets.push_back(subset);
	}
	return subsets;
}
```
