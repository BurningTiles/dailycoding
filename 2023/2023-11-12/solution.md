# Solution - 12 Nov 2023

---
## [815. Bus Routes](https://leetcode.com/problems/bus-routes)

### cpp
```cpp
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        const int INF = 501;
        vector<int> dist(1000000, INF); dist[source] = 0;
        vector<bool> visited(routes.size(), false);
        int count = 0, n = routes.size(), cnt=0;
        
        while(cnt < n && count < n) {
            for(int bus=0; bus<n; ++bus) {
                if (visited[bus]) continue;
                int min_dist = INF;
                
                for(auto i : routes[bus])
                    min_dist = min(min_dist, dist[i] + 1);
                
                for(auto i : routes[bus])
                    dist[i] = min(dist[i], min_dist);
                
                if (min_dist != INF)
                    visited[bus] = true, ++cnt;
            }
            count++;
        }

        return dist[target] == INF ? -1 : dist[target];
    }
};
```
