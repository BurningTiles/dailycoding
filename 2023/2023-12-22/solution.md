# Solution - 22 Dec 2023

---
## [1422. Maximum Score After Splitting a String](https://leetcode.com/problems/maximum-score-after-splitting-a-string)

### cpp
```cpp
class Solution {
public:
    int maxScore(string s) {
        int zero = 0, one = count(s.begin(), s.end(), '1'), ans = 0;
        
        for(int i=0; i<s.size()-1; ++i) {
            if(s[i]=='0') ++zero;
            else --one;
            ans = max(ans, zero + one);
        }

        return ans;
    }
};
```
