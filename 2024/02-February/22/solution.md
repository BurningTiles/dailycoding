# Solution - 22 Feb 2024

---
## [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge)

### cpp
```cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        int count[1001] = {0};
        
        for(auto &t:trust)
            --count[t[0]], ++count[t[1]];
        
        for(int i=1; i<1001; ++i)
            if(count[i]==n-1) return i;

        return -1;
    }
};
```
