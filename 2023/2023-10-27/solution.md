# Solution - 27 Oct 2023

---
## [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

### cpp
```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size(), maxLen = 0, index=0;
        for(int i=0; i<n; ++i) {
            int l=i-1, r=i+1, len;
            while(l>=0 && r<n && s[l]==s[r]) --l, ++r;
            len = r-l-1;
            if(len > maxLen)
                maxLen = len, index = l+1;
            
            l=i, r=i+1;
            while(l>=0 && r<n && s[l]==s[r]) --l, ++r;
            len = r-l-1;
            if(len > maxLen)
                maxLen = len, index = l+1;
        }
        return s.substr(index, maxLen);
    }
};
```
