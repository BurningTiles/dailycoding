# Solution - 11 May 2023

### [Square Root](https://workat.tech/problem-solving/practice/square-root) [(LeetCode)](https://leetcode.com/problems/sqrtx/)

```cpp
int searchRoot(int num) {
	long long ans = num;
	while(ans*ans>num)
		ans = (ans + num/ans)/2;
	return ans;
}
```

### [Remove occurences](https://workat.tech/problem-solving/practice/remove-occurences) [(LeetCode)](https://leetcode.com/problems/remove-element/)

```cpp
int removeOccurences(vector<int> &A, int k) {
	int ptr = 0;
	for(int i=0; i<A.size(); i++)
		if(A[i]!=k) A[ptr++] = A[i];
	return ptr;
}
```
