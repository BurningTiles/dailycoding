# Solution - 09 Nov 2024

---
## [3133. Minimum Array End](https://leetcode.com/problems/minimum-array-end)

### cpp
```cpp
class Solution {
public:
    long long minEnd(int n, int x) {
        long long ans = x, rem = n-1, pos = 1;

        while(rem) {
            if(!(x & pos)) {
                ans |= (rem & 1) * pos;
                rem >>= 1;
            }
            pos <<= 1;
        }

        return ans;
    }
};
```
