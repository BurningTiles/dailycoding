# Solution - 01 Mar 2024

---
## [2864. Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number)

### cpp
```cpp
class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        string ans(s.size(), '1');
        int i=s.size()-1;
        
        for(auto &ch:s)
            if(ch=='0') ans[--i] = ch;
        
        return ans;
    }
};
```
