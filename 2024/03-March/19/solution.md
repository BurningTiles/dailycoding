# Solution - 19 Mar 2024

---
## [621. Task Scheduler](https://leetcode.com/problems/task-scheduler)

### cpp
```cpp
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int cnt[26] = {0}, maxCnt = 0;
        
        for(auto &task:tasks)
            cnt[task-'A']++,
            maxCnt = max(maxCnt, cnt[task-'A']);
        
        int ans = (maxCnt-1) * (n+1);
        for(int i=0; i<26; ++i)
            if(cnt[i] == maxCnt) ++ans;
        
        return max((int)tasks.size(), ans);
    }
};
```
