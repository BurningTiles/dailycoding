# Solution - 01 Apr 2024

---
## [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word)

### cpp
```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size()-1, ans=0;

        while(i>=0 && s[i]==' ') --i;
        while(i>=0 && s[i]!=' ') --i, ++ans;
        
        return ans;
    }
};
```
