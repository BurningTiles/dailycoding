# Solution - 01 Jul 2025

---
## [3330. Find the Original Typed String I](https://leetcode.com/problems/find-the-original-typed-string-i)

### cpp
```cpp
class Solution {
public:
    int possibleStringCount(string word) {
        int ans = 1;

        for(int i=1; i<word.size(); ++i)
            if(word[i] == word[i-1])
                ++ans;

        return ans;
    }
};
```
