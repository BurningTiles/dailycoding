# Solution - 13 Jan 2024

---
## [1347. Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram)

### cpp
```cpp
class Solution {
public:
    int minSteps(string s, string t) {
        int count[128] = {0}, ans = 0;

        for(int i=0; i<s.size(); ++i)
            ++count[s[i]], --count[t[i]];
        
        for(int i=97; i<128; ++i)
            ans += abs(count[i]);

        return ans / 2;
    }
};
```
