# Solution - 27 Jan 2025

---
## [1462. Course Schedule IV](https://leetcode.com/problems/course-schedule-iv)

### cpp
```cpp
class Solution {
public:
    void bfs(vector<vector<int>> &courses, vector<vector<bool>> &reach, int index) {
        vector<bool> visited(courses.size(), false);
        queue<int> q;
        q.push(index);
        while(q.size()) {
            int size = q.size();
            for(int i=0; i<size; ++i) {
                int node = q.front(); q.pop();
                visited[node] = true;
                reach[node][index] = true;

                for(auto x:courses[node])
                    if(!visited[x])
                        q.push(x);
            }
        }
    }

    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<bool>> reach(numCourses, vector<bool>(numCourses, false));
        vector<vector<int>> courses(numCourses);
        vector<bool> ans;
        
        for(auto &pre:prerequisites)
            courses[pre[1]].push_back(pre[0]);
        
        for(int i=0; i<numCourses; ++i)
            bfs(courses, reach, i);

        for(auto &q:queries)
            ans.push_back(reach[q[0]][q[1]]);
        
        return ans;
    }
};
```
