# Solution - 03 Jun 2024

---
## [2486. Append Characters to String to Make Subsequence](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence)

### cpp
```cpp
class Solution {
public:
    int appendCharacters(string s, string t) {
        int m=s.size(), n=t.size(), i=0, j=0;

        while(i<m && j<n)
            if(s[i]==t[j]) ++i, ++j;
            else ++i;
        
        return n-j;
    }
};
```
