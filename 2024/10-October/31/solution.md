# Solution - 31 Oct 2024

---
## [2463. Minimum Total Distance Traveled](https://leetcode.com/problems/minimum-total-distance-traveled)

### cpp
```cpp
class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());

        int n = robot.size(), m = factory.size();
        vector<long long> dp(n + 1, 1000000000000000L);
        dp[0] = 0;

        for (int j = 0; j < m; ++j)
            for (int k = 0; k < factory[j][1]; ++k)
                for (int i = n - 1; i >= 0; --i)
                    dp[i + 1] = min(abs(robot[i] - factory[j][0]) + dp[i], dp[i + 1]);

        return dp[n];
    }
};
```
