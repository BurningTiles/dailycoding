# Solution - 05 Feb 2025

---
## [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal)

### cpp
```cpp
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int d1 = -1, d2 = -1;

        for(int i=0; i<s1.size(); ++i) {
            if(s1[i] != s2[i]) {
                if(d2 != -1) return false;
                d2 = d1;
                d1 = i;
            }
        }

        if(d1 != -1 && d2 == -1) return false;
        return d1 == -1 || (s1[d1] == s2[d2] && s1[d2] == s2[d1]);
    }
};
```
