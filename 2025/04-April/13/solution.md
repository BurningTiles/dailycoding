# Solution - 13 Apr 2025

---
## [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers)

### cpp
```cpp
#define MOD 1000000007
class Solution {
public:
    long long power(long long base, long long e, long long ans) {
        if(e==0) return ans;
        if(e & 1)
            return power(base, e-1, (ans * base) % MOD);
        else
            return power((base * base) % MOD, e / 2, ans);
    }

    int countGoodNumbers(long long n) {
        long long tmp = power(20, n/2, 1);
        return
            n & 1 ? (tmp * 5) % MOD : tmp;
    }
};
```
