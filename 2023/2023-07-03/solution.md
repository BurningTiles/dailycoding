# Solution - 03 Jul 2023

---
## [1. k-diff pairs](https://workat.tech/problem-solving/practice/k-diff-pairs) [(LeetCode)](https://leetcode.com/problems/k-diff-pairs-in-an-array/) 

### cpp
```cpp
int kDiffPairs(vector<int> &A, int k) {
	int i=0, j=1, ans=0;
	while(j<A.size()) {
		if(A[j]-A[i]==k) ++ans, ++i, ++j;
		else if(A[j]-A[i]<k) ++j;
		else ++i;
		while(j<A.size() && A[j]==A[j-1]) ++j;
		if(i==j) ++j;
	}
	return ans;
}
```


---
## [2. Kth element of two sorted lists](https://workat.tech/problem-solving/practice/kth-two-sorted) 

### cpp
```cpp
int getKthElement(vector<int> &firstArr, vector<int> &secondArr, int k) {
	int i=0, j=0;
	while(--k) {
		if(i<firstArr.size() && j<secondArr.size())
			firstArr[i]<secondArr[j] ? ++i : ++j;
		else ++i, ++j;
	}
	if(i<firstArr.size() && j<secondArr.size())
		return min(firstArr[i], secondArr[j]);
	return i<firstArr.size() ? firstArr[i] : secondArr[j];
}
```