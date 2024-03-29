# Solution - 20 Jul 2023

---
## [1. Longest Consecutive Sequence](https://workat.tech/problem-solving/practice/longest-consecutive-sequence) [(LeetCode)](https://leetcode.com/problems/longest-consecutive-sequence/) 

### cpp
```cpp
int longestConsecutiveSequence(vector<int> &A) {
	unordered_map<int, int> count;
	for(auto &x:A) ++count[x];
	int maxLen = 0, curLen = 0, val;
	for(int i=0; i<A.size(); i++) {
		if (count[A[i]-1]==1) continue;
		curLen = 0, val = A[i];
		while(count[val]) ++val, ++curLen;
		maxLen = max(maxLen, curLen);
	}
	return maxLen;
}

/*
// Another approach
int longestConsecutiveSequence(vector<int> &A) {
	sort(A.begin(), A.end());
	int curLen = 1, maxLen = 1;
	for(int i=1; i<A.size(); i++) {
		if(A[i]==A[i-1]) continue;
		if(A[i]==A[i-1]+1) ++curLen;
		else curLen = 1;
		maxLen = max(maxLen, curLen);
	}
	return maxLen;
}
*/
```


---
## [2. Longest Subarray with Zero Sum](https://workat.tech/problem-solving/practice/longest-subarray-zero-sum) 

### cpp
```cpp
int longestSubarrayWithZeroSum(vector<int> &A) {
	unordered_map<int, int> prefixSum;
	int maxLen = 0, curSum = 0;
	
	for(int i=0; i<A.size(); i++) {
		curSum += A[i];
		if(curSum == 0) maxLen = i+1;
		
		if(prefixSum.count(curSum))
			maxLen = max(maxLen, i-prefixSum[curSum]);
		else
			prefixSum[curSum] = i;
	}
	
	return maxLen;
}
```
