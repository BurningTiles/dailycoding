# Solution - 04 Jul 2025

---
## [3307. Find the K-th Character in String Game II](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii)

### cpp
```cpp
class Solution {
public:
    char kthCharacter(long long k, vector<int>& operations) {
        int ans = 0, n = operations.size();
        --k;

        for(int i=0; i<n && i<60; ++i)
            if((k>>i) & 1)
                ans += operations[i];
        
        return 'a' + ans % 26;
    }
};
```
