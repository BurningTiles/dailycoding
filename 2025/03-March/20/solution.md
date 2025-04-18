# Solution - 20 Mar 2025

---
## [3108. Minimum Cost Walk in Weighted Graph](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph)

### cpp
```cpp
class Solution {
public:
    vector<int> parent, minCost;

    int find(int node) {
        return parent[node] < 0 ? node : parent[node] = find(parent[node]);
    }

    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        parent = minCost = vector<int>(n, -1);

        for (auto &edge : edges) {
            int uRoot = find(edge[0]), vRoot = find(edge[1]);
            if (uRoot != vRoot) {
                minCost[uRoot] &= minCost[vRoot];
                parent[vRoot] = uRoot;
            }
            minCost[uRoot] &= edge[2];
        }

        vector<int> result;
        for (auto &q : query) {
            int uRoot = find(q[0]), vRoot = find(q[1]);
            if (q[0] == q[1]) result.push_back(0);
            else if (uRoot != vRoot) result.push_back(-1);
            else result.push_back(minCost[uRoot]);
        }

        return result;
    }
};
```
