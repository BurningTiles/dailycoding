# Solution - 19 Oct 2024

---
## [1545. Find Kth Bit in Nth Binary String](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string)

### cpp
```cpp
class Solution {
public:
    char findKthBit(int n, int k) {
        int flip = 0, l = (1 << n) - 1;

        while(k > 1) {
            if(k == l / 2 + 1)
                return '0' + !flip;
            if (k > l / 2) {
                k = l + 1 - k;
                flip = !flip;
            }
            l /= 2;
        }

        return '0' + flip;
    }
};
```
