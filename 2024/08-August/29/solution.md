# Solution - 29 Aug 2024

---
## [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column)

### cpp
```cpp
class Solution {
public:
    int dfs(vector<vector<int>> &stones, vector<bool> &visited, int index) {
        int ans = 0, n = stones.size();
        visited[index] = true;

        for(int i=0; i<n; ++i)
            if(!visited[i] && (stones[i][0] == stones[index][0] || stones[i][1] == stones[index][1]))
                ans += dfs(stones, visited, i) + 1;
        
        return ans;
    }

    int removeStones(vector<vector<int>>& stones) {
        int n = stones.size(), ans = 0;
        vector<bool> visited(n, false);

        for(int i=0; i<n; ++i) {
            if(visited[i]) continue;
            ans += dfs(stones, visited, i);
        }

        return ans;
    }
};
```
