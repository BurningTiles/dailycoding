# Solution - 28 Dec 2023

---
## [1531. String Compression II](https://leetcode.com/problems/string-compression-ii)

### cpp
```cpp
class Solution {
    inline int len(int n) {
        return n < 2 ? n : n < 10 ? 2 : n < 100 ? 3 : 4;
    }

public:
    int getLengthOfOptimalCompression(string s, int k) {
        int n = s.size(), dp[101][101]={};

        for(int i=1; i<=n; ++i) {
            for(int j=0; j<=i && j<=k; ++j) {
                int remove = 0, cnt = 0;
                dp[i][j] = INT_MAX;

                if (j) dp[i][j] = dp[i-1][j-1];

                for(int k=i; k>=1; --k) {
                    s[k-1] != s[i-1] ? ++remove : ++cnt;
                    
                    if (remove > j) break;

                    dp[i][j] = min(dp[i][j], dp[k-1][j-remove] + len(cnt));
                }
            }
        }

        return dp[n][k];
    }
};
```
