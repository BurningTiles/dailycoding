# Solution - 08 May 2025

---
## [3342. Find Minimum Time to Reach Last Room II](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii)

### cpp
```cpp
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size(), m = moveTime[0].size(), inf = INT_MAX;

        vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<vector<int>> dp(n, vector<int>(m, inf));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        pq.push({0,0,0,0});

        while(pq.size()) {
            auto x = pq.top(); pq.pop();
            int time = x[0], i = x[1], j = x[2], alt = x[3];

            if(i==n-1 && j==m-1)
                return time;
            if(time >= dp[i][j])
                continue;
            dp[i][j] = time;
            
            for(auto [x, y]:dir) {
                x += i, y += j;
                if(x >= 0 && y >= 0 && x < n && y < m && dp[x][y]==inf)
                    pq.push({max(time, moveTime[x][y]) + 1 + alt, x, y, !alt});
            }
        }

        return -1;
    }
};
```
