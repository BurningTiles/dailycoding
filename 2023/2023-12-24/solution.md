# Solution - 24 Dec 2023

---
## [1758. Minimum Changes To Make Alternating Binary String](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string)

### cpp
```cpp
class Solution {
public:
    int minOperations(string s) {
        int chg01=0;

        for(int i=0; i<s.size(); ++i)
            if(s[i]-'0' != (i&1)) ++chg01;

        return min(chg01, int(s.size()-chg01));
    }
};
```
