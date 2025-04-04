# Solution - 31 Dec 2024

---
## [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets)

### cpp
```cpp
class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        queue<pair<int, int>> last7, last30;
        int cost = 0;

        for(int i=0; i<days.size(); ++i) {
            while(last7.size() && last7.front().first + 7 <= days[i])
                last7.pop();
            while(last30.size() && last30.front().first + 30 <= days[i])
                last30.pop();
            
            last7.push({days[i], cost + costs[1]});
            last30.push({days[i], cost + costs[2]});

            cost = min({cost + costs[0], last7.front().second, last30.front().second});
        }

        return cost;
    }
};
```
