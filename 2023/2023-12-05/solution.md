# Solution - 05 Dec 2023

---
## [1688. Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament)

### cpp
```cpp
class Solution {
public:
    int numberOfMatches(int n) {
        int ans=0;
        while(n>1) {
            ans += n/2;
            n = (n+1)/2;
        }
        return ans;
    }
};
```
