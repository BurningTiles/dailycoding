# Solution - 11 Mar 2024

---
## [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string)

### cpp
```cpp
class Solution {
public:
    string customSortString(string order, string s) {
        int count[128] = {0};
        for(auto ch:s) ++count[ch];

        string ans="";
        for(auto ch:order)
            if(count[ch])
                ans += string(count[ch], ch), 
                count[ch] = 0;
        
        for(int i=97; i<123; ++i)
            if(count[i])
                ans += string(count[i], i);

        return ans;
    }
};
```
