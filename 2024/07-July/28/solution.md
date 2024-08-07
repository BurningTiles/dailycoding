# Solution - 28 Jul 2024

---
## [2045. Second Minimum Time to Reach Destination](https://leetcode.com/problems/second-minimum-time-to-reach-destination)

### cpp
```cpp
class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        unordered_map<int, list<int>> g;
        for (const auto &e:edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        q.push({0, 1});

        vector<int> uniqueVisit(n+1, 0);
        vector<int> dis(n+1, -1);

        while(q.size()) {
            auto [t, node] = q.top(); q.pop();

            if(dis[node] == t || uniqueVisit[node] >= 2)
                continue;
            
            ++uniqueVisit[node];
            dis[node] = t;

            if(node == n && uniqueVisit[node] == 2)
                return dis[node];
            
            if((t / change) % 2 != 0)
                t = (t / change + 1) * change;

            for(int ne: g[node])
                q.push({t + time, ne});
        }

        return -1;
    }
};
```
