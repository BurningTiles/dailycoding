# Solution - 06 Sep 2023

---
## [1. Matrix Paths](https://workat.tech/problem-solving/practice/matrix-paths) [(LeetCode)](https://leetcode.com/problems/unique-paths/) 

### cpp
```cpp
int getNumPaths(int rows, int columns) {
	long long ans = 1, n = rows+columns-2;
	for(int i=1; i<min(rows, columns); i++)
		ans *= n--, ans /= i;
	return ans;
}

/*
// Dynamic Programming
int getNumPaths(int rows, int columns) {
	int dp[rows+1][columns+1];
	for(int i=0; i<=rows; i++) dp[i][0] = 0;
	for(int i=0; i<=columns; i++) dp[0][i] = 0;
	dp[0][1] = 1;
	for(int i=1; i<=rows; i++)
		for(int j=1; j<=columns; j++)
			dp[i][j] = dp[i-1][j] + dp[i][j-1];
	return dp[rows][columns];
}
*/
```
