# Solution - 21 Jul 2024

---
## [2392. Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> buildMatrix(int k, vector<vector<int>>& rowConditions, vector<vector<int>>& colConditions) {
        vector<vector<int>> rowGraph(k+1), colGraph(k+1);

        for(auto &rc:rowConditions)
            rowGraph[rc[0]].push_back(rc[1]);

        for(auto &cc:colConditions)
            colGraph[cc[0]].push_back(cc[1]);

        vector<int> rowOrder = topSort(rowGraph, k);
        vector<int> colOrder = topSort(colGraph, k);

        if(rowOrder.empty() || colOrder.empty()) return {};

        vector<vector<int>> ans(k, vector<int>(k, 0));\

        unordered_map<int, int> rowMap, colMap;

        for(int i=0; i<k; ++i) {
            rowMap[rowOrder[i]] = i;
            colMap[colOrder[i]] = i;
        }

        for(int i=1; i<=k; ++i)
            ans[rowMap[i]][colMap[i]] = i;
        
        return ans;
    }

    vector<int> topSort(vector<vector<int>> &graph, int k){
        vector<int> inDegree(k+1, 0), order;
        queue<int> q;

        for(int i=1; i<=k; ++i)
            for(int j:graph[i]) 
                ++inDegree[j];
        
        for(int i=1; i<=k; ++i)
            if(inDegree[i] == 0)
                q.push(i);
        
        while(q.size()) {
            int n = q.front(); q.pop();
            order.push_back(n);
            for(int adj:graph[n])
                if(--inDegree[adj] == 0)
                    q.push(adj);
        }

        if(order.size() == k)
            return order;
            
        return {};
    }
};
```
