# Solution - 09 Jun 2025

---
## [440. K-th Smallest in Lexicographical Order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order)

### cpp
```cpp
class Solution {
public:
    int findKthNumber(int n, int k) {
        int ans = 1;

        for (int i=--k; i > 0;) {
            int count = 0;
            for (long long first = static_cast<long long>(ans),
                           last = first + 1;
                 first <= n; first *= 10, last *= 10) {
                count += static_cast<int>((min(n + 1LL, last) - first));
            }

            if (i >= count) {
                ++ans;
                i -= count;
            } else {
                ans *= 10;
                --i;
            }
        }

        return ans;
    }
};
```
