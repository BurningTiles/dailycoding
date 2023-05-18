# Solution - 15 May 2023

---
## [1. Unique Elements in Sorted Array](https://workat.tech/problem-solving/practice/unique-elements-sorted-array) [(LeetCode)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 

```cpp
int removeDuplicates(vector<int> &A) {
    int ans = A.size() ? 1 : 0;
	for(int i=1; i<A.size(); i++)
		if(A[i]!=A[i-1]) ++ans;
	return ans;
}
```

---
## [2. Sorted Arrays Intersection](https://workat.tech/problem-solving/practice/sorted-arrays-intersection) 

```cpp
vector<int> intersection(vector<int> &A, vector<int> &B) {
	vector<int> ans;
	int i=0, j=0;
	while(i<A.size() && j<B.size()) {
		if(A[i]<B[j]) ++i;
		else if(A[i]>B[j]) ++j;
		else ans.push_back(A[i]), ++i, ++j;
	}
	return ans;
}
```