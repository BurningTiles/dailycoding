# Solution - 30 Nov 2024

---
## [2097. Valid Arrangement of Pairs](https://leetcode.com/problems/valid-arrangement-of-pairs)

### cpp
```cpp
class Solution {
public:
    map<int, vector<int> > adj;
    vector<vector<int> > ans;
    
    void dfs(int node) {
        while(adj[node].size()) {
            int next = adj[node].back();
            adj[node].pop_back();
            dfs(next);
            ans.push_back({node, next});
        }
    }
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        map<int, int> indegree;
        for(auto &p : pairs) {
            adj[p[0]].push_back(p[1]);
            ++indegree[p[0]];
            --indegree[p[1]];
        }
        int start = -1;
        for(auto &it: indegree) {
            if(it.second >0) start = it.first;
        }
        if(start == -1) {
            start = pairs[0][0];
        }
        dfs(start);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```
