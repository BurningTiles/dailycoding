# Solution - 03 Nov 2024

---
## [796. Rotate String](https://leetcode.com/problems/rotate-string)

### cpp
```cpp
class Solution {
public:
    bool rotateString(string s, string goal) {
        if(s.size() != goal.size())
            return false;
        return (s + s).find(goal) != string::npos;
    }
};
```
