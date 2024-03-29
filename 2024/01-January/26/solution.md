# Solution - 26 Jan 2024

---
## [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths)

### cpp
```cpp
#define mod 1000000007

class Solution {
public:
    int dp[51][51][51];

    long long helper(int m, int n, int N, int i, int j) {
        if(i<0 || j<0 || i>=m || j>=n) return 1;
        if(N <= 0) return 0;
        if(dp[i][j][N] != -1) return dp[i][j][N];

        long long ans = 0;
        ans = helper(m, n, N-1, i-1, j) + helper(m, n, N-1, i+1, j) +
            helper(m, n, N-1, i, j-1) + helper(m, n, N-1, i, j+1);
        
        return dp[i][j][N] = ans % mod;
    }

    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        memset(dp, -1, sizeof(dp));
        return helper(m, n, maxMove, startRow, startColumn) % mod;
    }
};
```
