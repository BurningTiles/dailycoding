# Solution - 10 Jul 2024

---
## [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int depth = 0;

        for(auto &log:logs) {
            if(log == "../") --depth;
            else if(log != "./") ++depth;
            
            if(depth < 0) 
                depth = 0;
        }

        return depth;
    }
};
```
