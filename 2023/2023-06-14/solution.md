# Solution - 14 Jun 2023

---
## [1. Most Significant Bit](https://workat.tech/problem-solving/practice/most-significant-bit) 

```cpp
int msbSignificance(int n) {
	return 1 << int(log2(n));
}

/*
 * Other solution
int msbSignificance(int n) {
	int cnt=0;
	while(n)
		n /= 2, ++cnt;
	return 1 << (cnt-1);
}
*/
```

---
## [2. Power Of Two](https://workat.tech/problem-solving/practice/power-of-two) [(LeetCode)](https://leetcode.com/problems/power-of-two/) 

```cpp
bool isPowerOfTwo(int n) {
	return n > 0 && ! (n & n-1);
}
```