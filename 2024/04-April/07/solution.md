# Solution - 07 Apr 2024

---
## [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string)

### cpp
```cpp
class Solution {
public:
    bool checkValidString(string s) {
        int high=0, low=0;
        
        for(int i=0; i<s.size(); ++i) {
            high += (s[i]=='(' || s[i]=='*') ? 1 : -1;
            low += (s[i]==')' || s[i]=='*') ? -1 : 1;
            if(high<0) return false;
            low = max(0, low);
        }

        return low==0;
    }
};
```
