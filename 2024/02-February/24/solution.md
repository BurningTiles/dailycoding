# Solution - 24 Feb 2024

---
## [2092. Find All People With Secret](https://leetcode.com/problems/find-all-people-with-secret)

### cpp
```cpp
class Solution {
public:
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<pair<int, int>> adj[n];
        
        for(auto &m:meetings)
            adj[m[0]].push_back({m[1], m[2]}),
            adj[m[1]].push_back({m[0], m[2]});

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        pq.push({0, firstPerson});
        vector<bool> visited(n, false);

        while(pq.size()) {
            auto [time, person] = pq.top(); pq.pop();
            
            if(visited[person]) continue;
            visited[person] = true;

            for(auto &m:adj[person])
                if(!visited[m.first] && m.second >= time)
                    pq.push({m.second, m.first});
        }

        vector<int> ans;
        for(int i=0; i<n; ++i) 
            if(visited[i]) 
                ans.push_back(i);
            
        return ans;
    }
};
```
