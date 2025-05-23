# Solution - 07 May 2025

---
## [3341. Find Minimum Time to Reach Last Room I](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i)

### cpp
```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int ans = 0, n = moveTime.size(), m = moveTime[0].size();

        vector<vector<int>> dp(n, vector<int>(m, INT_MAX));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({0, 0, 0});

        vector<pair<int, int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while(pq.size()) {
            auto x = pq.top(); pq.pop();
            int t = x[0], i = x[1], j = x[2];

            if(t >= dp[i][j]) continue;
            if(i == n - 1 && j == m - 1) return t;
            dp[i][j] = t;

            for(auto [x, y]:dirs) {
                x += i, y += j;
                if(x >= 0 && x < n && y >= 0 && y < m && dp[x][y] == INT_MAX)
                    pq.push({max(moveTime[x][y], t) + 1, x, y});
            }
        }

        return -1;
    }
};
```
