# Solution - 04 Apr 2024

---
## [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses)

### cpp
```cpp
class Solution {
public:
    int maxDepth(string s) {
        int ans = 0, cur = 0;

        for(int i=0; i<s.size(); ++i)
            if(s[i]=='(') ans = max(ans, ++cur);
            else if(s[i]==')') --cur;

        return ans;
    }
};
```
