# Solution - 11 Jan 2025

---
## [1400. Construct K Palindrome Strings](https://leetcode.com/problems/construct-k-palindrome-strings)

### cpp
```cpp
class Solution {
public:
    bool canConstruct(string s, int k) {
        bitset<26> odd;
        for (char& c : s)
            odd.flip(c - 'a');
        return odd.count() <= k && k <= s.length();
    }
};
```
