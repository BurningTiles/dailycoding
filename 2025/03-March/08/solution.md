# Solution - 08 Mar 2025

---
## [2379. Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks)

### cpp
```cpp
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int maxBlack = 0, curBlack = 0;
        
        for(int i=0; i<k-1; ++i)
            curBlack += blocks[i] == 'B';
        
        for(int i=k-1, j=0; i<blocks.size(); ++i, ++j) {
            curBlack += blocks[i] == 'B';
            maxBlack = max(maxBlack, curBlack);
            curBlack -= blocks[j] == 'B';
        }

        return k - maxBlack;
    }
};
```
