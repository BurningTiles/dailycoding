# Solution - 03 Jul 2025

---
## [3304. Find the K-th Character in String Game I](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i)

### cpp
```cpp
class Solution {
public:
    char kthCharacter(int k) {
        return 'a' + __builtin_popcount(k-1);
    }
};
```
