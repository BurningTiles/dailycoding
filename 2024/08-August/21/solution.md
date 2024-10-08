# Solution - 21 Aug 2024

---
## [664. Strange Printer](https://leetcode.com/problems/strange-printer)

### cpp
```cpp
class Solution {
public:
    int helper(int i, int j, const string &s, vector<vector<int>> &dp) {
        if(i>j) return 0;

        if(dp[i][j] != -1)
            return dp[i][j];
        
        char firstChar = s[i];

        int ans = 1 + helper(i+1, j, s, dp);
        for(int k=i+1; k<=j; ++k) {
            if(s[k] == firstChar) {
                int tmp = helper(i, k-1, s, dp) + helper(k+1, j, s, dp);
                ans = min(ans, tmp);
            }
        }

        return dp[i][j] = ans;
    }

    int strangePrinter(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return helper(0, n-1, s, dp);
    }
};
```
