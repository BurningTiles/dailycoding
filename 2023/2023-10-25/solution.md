# Solution - 25 Oct 2023

---
## [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar)

### cpp
```cpp
class Solution {
public:
    int solve(int k, int x=1<<30) {
        if(k<2) return k;
        while(x > k) x >>= 1;
        return !solve(k-x, x);
    }

    int kthGrammar(int n, int k) {
        return solve(k-1);
    }
};
```
