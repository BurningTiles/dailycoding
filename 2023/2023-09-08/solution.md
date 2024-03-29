# Solution - 08 Sep 2023

---
## [1. Repeat and Missing Number in Array](https://workat.tech/problem-solving/practice/repeat-and-missing-number-array) 

### cpp
```cpp
vector<int> findRepeatAndMissingNumber(vector<int> &nums) {
	long long n = nums.size(), sum = (n*(n+1))/2, sum_sq = (n*(n+1)*(2*n+1))/6;
	for(auto &num:nums)
		sum -= num, sum_sq -= num * num;
	long long missing = (sum+sum_sq/sum)/2;
	return {missing - sum, missing};
}

/*
// Another approach
vector<int> findRepeatAndMissingNumber(vector<int> &nums) {
	int mark[nums.size()+1] = {0}, x, y;
	for(auto &num:nums) mark[num]++;
	for(int i=1; i<=nums.size(); i++)
		if(mark[i]==2) x = i;
		else if(!mark[i]) y = i;
	return {x, y};
}
*/
```
