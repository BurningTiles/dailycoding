# Solution - 05 Dec 2024

---
## [2337. Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string)

### cpp
```cpp
class Solution {
public:
    bool canChange(string start, string target) {
        int n = start.size(), j=0;
        
        for(int i=0; i<n; ++i) {
            if(target[i]=='_')
                continue;
            while(j<n && start[j]=='_') ++j;

            if(target[i] != start[j]) return false;
            if((i>j && start[j]=='L') || (i<j && start[j]=='R'))
                return false;
            else ++j;
        }

        while(j<n)
            if(start[j] != '_') return false;
            else ++j;

        return true;
    }
};
```
