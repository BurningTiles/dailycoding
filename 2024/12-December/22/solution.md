# Solution - 22 Dec 2024

---
## [2940. Find Building Where Alice and Bob Can Meet](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet)

### cpp
```cpp
// Reference: https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/solutions/4304269/javacpython-priority-queue-by-lee215-11js/

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        int n = heights.size(), qn = queries.size();
        vector<vector<vector<int>>> que(n);
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<int> ans(qn, -1);

        for(int qi = 0; qi < qn; ++qi) {
            int i = queries[qi][0], j = queries[qi][1];
            if(i<j && heights[i]<heights[j])
                ans[qi] = j;
            else if(i>j && heights[i]>heights[j])
                ans[qi] = i;
            else if(i==j)
                ans[qi] = i;
            else
                que[max(i, j)].push_back({max(heights[i], heights[j]), qi});
        }

        for(int i=0; i<n; ++i) {
            while(!pq.empty() && pq.top()[0]<heights[i]){
                ans[pq.top()[1]] = i;
                pq.pop();
            }
            for(auto &q:que[i])
                pq.push(q);
        }

        return ans;
    }
};
```
