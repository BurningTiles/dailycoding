# Solution - 11 Sep 2023

---
## [1. Divide without Division, Multiplication & Mod](https://workat.tech/problem-solving/practice/divide-without-division-multiplication-mod) [(LeetCode)](https://leetcode.com/problems/divide-two-integers/) 

### cpp
```cpp
int divide(int a, int b) {
	bool sign=(a<0) ^ (b<0);
	long long x = abs(a), y = abs(b), ans = 0, temp = 0;
	for (int i = 31; i >= 0; --i) {
		if (temp + (y << i) <= x) {
			temp += y << i;
			ans |= 1LL << i;
		}
	}
	if(sign) ans =- ans;
	return ans;
}
```
