# Solution - 10 Feb 2024

---
## [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings)

### cpp
```cpp
class Solution {
public:
    int countPal(string &s, int l, int r) {
        while(l>=0 && r<s.size() && s[l]==s[r])
            --l, ++r;
        return (r-l)/2;
    }

    int countSubstrings(string s) {
        int ans = 0;

        for(int i=0; i<s.size(); ++i)
            ans += countPal(s, i-1, i+1) + countPal(s, i, i+1);

        return ans;
    }
};
```
