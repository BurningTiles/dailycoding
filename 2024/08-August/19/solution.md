# Solution - 19 Aug 2024

---
## [650. 2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard)

### cpp
```cpp
class Solution {
public:
    int minSteps(int n) {
        int ans = 0;

        for(int prime = 2; prime <= n; ++prime) {
            while(n % prime == 0) {
                ans += prime;
                n /= prime;
            }
        }

        return ans;
    }
};
```
