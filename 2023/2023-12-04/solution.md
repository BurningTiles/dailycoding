# Solution - 04 Dec 2023

---
## [2264. Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string)

### cpp
```cpp
class Solution {
public:
    string largestGoodInteger(string num) {
        char ch=0;
        for(int i=2; i<num.size(); ++i)
            if(num[i]==num[i-1] && num[i]==num[i-2] && num[i]>ch)
                ch = num[i];
        return ch ? string(3, ch) : "";
    }
};
```
