# Solution - 12 Sep 2023

---
## [1. Square without Multiplication, Division & Pow](https://workat.tech/problem-solving/practice/square-without-multiply-divide-pow) 

### cpp
```cpp
int findSquare(int num) {
	int ans = 0, cur = num;
	while(num) {
		if(num&1) ans += cur;
		num >>= 1;
		cur <<= 1;
	}
	return ans;
}
```
