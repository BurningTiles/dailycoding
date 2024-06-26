# Solution - 29 Jun 2024

---
## [2192. All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph)

### cpp
```cpp
class Solution {
public:
    void dfs(int node, int curNode, vector<vector<int>> &ans, vector<vector<int>> &childs) {
        for(auto &child:childs[curNode])
            if(ans[child].size() == 0 || ans[child].back() != node) {
                ans[child].push_back(node);
                dfs(node, child, ans, childs);
            }
    }

    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> ans(n), childs(n);

        for(auto &e: edges)
            childs[e[0]].push_back(e[1]);
        
        for(int i=0; i<n; ++i)
            dfs(i, i, ans, childs);
        
        return ans;
    }
};
```
