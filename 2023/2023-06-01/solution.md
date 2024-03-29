# Solution - 01 Jun 2023

---
## [1. Implement Counting Sort](https://workat.tech/problem-solving/practice/implement-counting-sort) 

```cpp
void countingSort(vector<int> &arr) {
	int count[2002] = {0};
	for(auto &x: arr)
		++count[x+1000];
	for(int i=0, j=0; i<2002; ++i)
		while(count[i]--)
			arr[j++] = i-1000;
}
```

---
## [2. Two Sum](https://workat.tech/problem-solving/practice/two-sum) [(LeetCode)](https://leetcode.com/problems/two-sum/) 

```cpp
pair<int,int> twoSum(vector<int> &A, int target) {
	int n = A.size();
	vector<pair<int, int>> v(n);
	for(int i=0; i<n; i++)
		v[i] = {A[i], i};
	sort(v.begin(), v.end());
	
	int i=0, j=n-1, sum;
	while(i<j) {
		sum = v[i].first + v[j].first;
		if(sum==target)
			return {v[i].second, v[j].second};
		sum < target ? ++i : --j;
	}
	return {-1, -1};
}
```