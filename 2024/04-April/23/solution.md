# Solution - 23 Apr 2024

---
## [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees)

### cpp
```cpp
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if(n==1) return {0};
	    if(n==2) return edges[0];
	    vector<vector<int>> graph(n);
	    vector<int> indegree(n, 0), ans;
	    
	    for(auto &e:edges){
	        graph[e[0]].push_back(e[1]);
	        graph[e[1]].push_back(e[0]);
	        indegree[e[0]]++;
	        indegree[e[1]]++;
	    }

	    queue<int> q;
	    for(int i=0; i<n; i++)
	        if(indegree[i]==1) q.push(i), indegree[i]--;
	    
	    while(!q.empty()){
	        int s = q.size();
	        ans.clear();
	        for(int i=0; i<s; i++){
	            int cur = q.front(); q.pop();
	            ans.push_back(cur);
	            for(auto child:graph[cur]){
	                indegree[child]--;
	                if(indegree[child]==1) q.push(child);
	            }
	        }
	    }
	    return ans;
    }
};
```
