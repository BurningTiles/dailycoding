# Solution - 08 Jul 2024

---
## [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game)

### cpp
```cpp
class Solution {
public:
    int findTheWinner(int n, int k) {
        int res = 0;
        for (int player_num = 2; player_num <= n; ++player_num) {
            res = (res + k) % player_num;
        }
        return res + 1;
    }
};
```
