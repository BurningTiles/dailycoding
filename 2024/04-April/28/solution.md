# Solution - 28 Apr 2024

---
## [834. Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree)

### cpp
```cpp
class Solution {
    vector<unordered_set<int>> tree;
    vector<int> res, count;

    void dfs(int root, int pre) {
        for(auto i:tree[root]) {
            if(i==pre) continue;
            dfs(i, root);
            count[root] += count[i];
            res[root] += res[i] + count[i];
        }
    }

    void dfs2(int root, int pre) {
        for(auto i:tree[root]) {
            if(i==pre) continue;
            res[i] = res[root] - count[i] + count.size() - count[i];
            dfs2(i, root);
        }
    }
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        tree.resize(n);
        res.assign(n, 0);
        count.assign(n, 1);
        
        for(auto e:edges) {
            tree[e[0]].insert(e[1]);
            tree[e[1]].insert(e[0]);
        }
        dfs(0, -1);
        dfs2(0, -1);
        return res;
    }
};
```
