# Solution - 14 Jun 2025

---
## [2566. Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit)

### cpp
```cpp
class Solution {
public:
    int minMaxDifference(int num) {
        string s = to_string(num), large = s, small = s;
        char dl = -1, ds = -1;

        for(int i=0; i<s.size(); ++i) {
            if(dl == -1 && s[i] != '9')
                dl = s[i], large[i] = '9';
            else if(s[i] == dl)
                large[i] = '9';
            
            if(ds == -1 && s[i] != '0')
                ds = s[i], small[i] = '0';
            else if(s[i] == ds)
                small[i] = '0';
        }

        return stoi(large) - stoi(small);
    }
};
```
