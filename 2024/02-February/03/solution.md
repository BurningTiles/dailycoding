# Solution - 03 Feb 2024

---
## [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum)

### cpp
```cpp
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size(), dp[n+1];
        
        for (int i = 0; i <= n; ++i) {
            int curMax = 0; dp[i] = 0;
            for (int j = 1; j <= k && i - j >= 0; ++j)
                curMax = max(curMax, arr[i - j]),
                dp[i] = max(dp[i], dp[i - j] + curMax * j);
        }

        return dp[n];
    }
};
```
