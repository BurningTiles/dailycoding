# Solution - 18 Feb 2025

---
## [2375. Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string)

### cpp
```cpp
class Solution {
public:
    string smallestNumber(string pattern) {
        string ans, stk;

        for(int i=0; i<=pattern.size(); ++i) {
            stk.push_back('1' + i);
            if(i == pattern.size() || pattern[i] == 'I') {
                while(!stk.empty()) {
                    ans.push_back(stk.back());
                    stk.pop_back();
                }
            }
        }

        return ans;
    }
};
```
