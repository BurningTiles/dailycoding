# Solution - 02 Apr 2024

---
## [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings)

### cpp
```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int map1[128] = {0}, map2[128] = {0}, n = s.size();

        for(int i=0; i<n; ++i)
            if(map1[s[i]] != map2[t[i]]) return false;
            else map1[s[i]] = map2[t[i]] = i+1;

        return true;
    }
};
```
