# Solution - 05 Sep 2023

---
## [1. Primes upto N](https://workat.tech/problem-solving/practice/primes-upto-n) [(LeetCode)](https://leetcode.com/problems/count-primes/) 

### cpp
```cpp
vector<int> primesUptoN(int n) {
	if(n<2) return 0;
	bool mark[n+1];
	for(int i=0; i<=n; i++) mark[i] = true;
	mark[0] = mark[1] = false;
	for(int i=2; i*i<=n; i++) {
		if(mark[i]) {
			for(int j=i*i; j<=n; j+=i)
				mark[j] = false;
		}
	}
	vector<int> ans;
	for(int i=2; i<=n; i++) if(mark[i]) ans.push_back(i);
	return ans;
}
```
