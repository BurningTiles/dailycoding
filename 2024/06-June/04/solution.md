# Solution - 04 Jun 2024

---
## [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome)

### cpp
```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int cnt[128] = {0}, ans = 0;

        for(int i=0; i<s.size(); ++i)
            cnt[s[i]]++;

        for(int i=65; i<124; ++i)
            ans += cnt[i]&1 ? cnt[i]-1 : cnt[i];

        return ans < s.size() ? ans + 1 : ans;        
    }
};
```
