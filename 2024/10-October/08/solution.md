# Solution - 08 Oct 2024

---
## [1963. Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced)

### cpp
```cpp
class Solution {
public:
    int minSwaps(string s) {
        int ans = 0;

        for(int i=0; i<s.size(); ++i) {
            if(s[i] == '[')
                ++ans;
            else if(ans != 0)
                --ans;
        }

        return (ans + 1) / 2;
    }
};
```
