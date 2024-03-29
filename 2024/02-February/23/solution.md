# Solution - 23 Feb 2024

---
## [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops)

### cpp
```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int, vector<pair<int, int>>> adj;
        
        for(auto &f:flights)
            adj[f[0]].push_back({f[1], f[2]});

        vector<int> dist(n, INT_MAX);
        dist[src] = 0; ++k;

        queue<pair<int, int>> q;
        q.push({src, 0});

        while(q.size() && k--) {
            int size = q.size();
            while(size--) {
                auto [node, distance] = q.front(); q.pop();
                if(!adj.count(node)) continue;

                for(auto &[neighbour, price]:adj[node]) {
                    if(price + distance >= dist[neighbour]) continue;
                    dist[neighbour] = price + distance;
                    q.push({neighbour, dist[neighbour]});
                }
            }
        }

        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};
```
