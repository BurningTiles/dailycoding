# Solution - 05 Mar 2024

---
## [1750. Minimum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends)

### cpp
```cpp
class Solution {
public:
    int minimumLength(string s) {
        int l=0, r=s.size()-1;

        while(s[l]==s[r] && l<r) {
            char ch = s[l];
            while(l<=r && s[l]==ch) ++l;
            while(r>=l && s[r]==ch) --r;
        }

        return r-l+1;
    }
};
```
