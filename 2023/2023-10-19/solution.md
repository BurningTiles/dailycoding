# Solution - 19 Oct 2023

---
## [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare)

### cpp
```cpp
class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s1 = "", s2 = "";
        for(auto &ch:s) 
            if(ch=='#') { if(s1.size()) s1.pop_back(); }
            else s1.push_back(ch);
        for(auto &ch:t)
            if(ch=='#') { if(s2.size()) s2.pop_back(); }
            else s2.push_back(ch);
        return s1==s2;
    }
};
```
