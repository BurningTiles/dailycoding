# Solution - 07 Dec 2023

---
## [1903. Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string)

### cpp
```cpp
class Solution {
public:
    string largestOddNumber(string num) {
        for(int i=num.size()-1; i>=0; --i)
            if(num[i] & 1)
                return num.substr(0, i+1);
        return "";
    }
};
```
