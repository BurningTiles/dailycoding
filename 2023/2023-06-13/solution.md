# Solution - 13 Jun 2023

---
## [1. Trailing Zeroes](https://workat.tech/problem-solving/practice/trailing-zeroes) [(LeetCode)](https://leetcode.com/problems/factorial-trailing-zeroes/) 

```cpp
int trailingZeroesInFactorial(int n) {
	int ans = 0;
	while(n)
		n /= 5, ans += n;
	return ans;
}
```

---
## [2. Greatest Common Divisor](https://workat.tech/problem-solving/practice/gcd) [(LeetCode)](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) 

```cpp
int gcd(int firstNum, int secondNum) {
	return firstNum % secondNum == 0 ? secondNum : gcd(secondNum, firstNum % secondNum);
}

/*

int gcd(int firstNum, int secondNum) {
	while(secondNum) {
		int tmp = firstNum % secondNum;
		firstNum = secondNum;
		secondNum = tmp;
	}
	return firstNum;
}

*/
```