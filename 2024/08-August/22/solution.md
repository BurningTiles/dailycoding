# Solution - 22 Aug 2024

---
## [476. Number Complement](https://leetcode.com/problems/number-complement)

### cpp
```cpp
class Solution {
public:
    int findComplement(int num) {
        long long ans = 0, mul = 1;

        do {
            ans += num&1 ? 0 : mul;
            num /= 2;
            mul *= 2;
        } while(num);

        return ans;
    }
};
```
