# Solution - 06 Jul 2024

---
## [2582. Pass the Pillow](https://leetcode.com/problems/pass-the-pillow)

### cpp
```cpp
class Solution {
public:
    int passThePillow(int n, int time) {
        int r = (n - 1) * 2, i = time % r, ans = i < n ? i + 1 : 2 * n - i - 1;
        return ans;
    }
};
```
