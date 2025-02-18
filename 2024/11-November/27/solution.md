# Solution - 27 Nov 2024

---
## [3243. Shortest Distance After Road Addition Queries I](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i)

### cpp
```cpp
class Solution {
public:
    int shortestPath(vector<vector<int>> &adj, int n) {
        queue<pair<int, int>> q;
        q.push({0, 0});
        unordered_set<int> visit;
        visit.insert(0);

        while(q.size()) {
            auto [cur, len] = q.front();
            q.pop();

            if(cur == n-1) return len;

            for(int i:adj[cur]) {
                if(!visit.count(i)) {
                    q.push({i, len + 1});
                    visit.insert(i);
                }
            }
        }

        return -1;
    }

    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        vector<vector<int>> adj(n);
        for(int i=0; i<n; ++i)
            adj[i].push_back(i+1);
        
        vector<int> ans;

        for(auto &q:queries) {
            adj[q[0]].push_back(q[1]);
            ans.push_back(shortestPath(adj, n));
        }
        
        return ans;
    }
};
```
