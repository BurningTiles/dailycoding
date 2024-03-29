# Solution - 08 Oct 2023

---
## [1458. Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences)

### cpp
```cpp
class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size(), dp[m+1][n+1];
        for(int i=0; i<=m; i++) dp[i][0] = -9999;
        for(int j=0; j<=n; j++) dp[0][j] = -9999;
        for(int i=1; i<=m; i++) {
            for(int j=1; j<=n; j++) {
                dp[i][j] = max({
                    dp[i-1][j], dp[i][j-1],
                    max(dp[i-1][j-1], 0) + nums1[i-1]*nums2[j-1]});
            }
        }
        return dp[m][n];
    }
};
```
