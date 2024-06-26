# Solution - 21 Apr 2024

---
## [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph)

### cpp
```cpp
class Solution {
    int *par;
public:
    int parent(int x) {
        return par[x]==x ? x : (par[x] = parent(par[x]));
    }

    void makeGroup(int a, int b) {
        int x = parent(a), y = parent(b);
        par[x] = y;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        par = new int[n];
        for(int i=0; i<n; ++i) par[i] = i;

        for(auto &e:edges)
            makeGroup(e[0], e[1]);
        
        return parent(source) == parent(destination);
    }
};
```
