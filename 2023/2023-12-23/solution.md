# Solution - 23 Dec 2023

---
## [1496. Path Crossing](https://leetcode.com/problems/path-crossing)

### cpp
```cpp
class Solution {
public:
    inline string toStr(int x, int y) { return to_string(x) + "|" + to_string(y); }
    
    bool isPathCrossing(string path) {
        unordered_set<string> us;
        int x=0, y=0;
        us.insert(toStr(x, y));

        for(auto ch:path) {
            if(ch=='N') ++y;
            else if(ch=='E') --x;
            else if(ch=='W') ++x;
            else --y;

            if(!us.insert(toStr(x, y)).second)
                return true;
        }
        
        return false;
    }
};
```
