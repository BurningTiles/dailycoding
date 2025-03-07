# Solution - 07 Mar 2025

---
## [2523. Closest Prime Numbers in Range](https://leetcode.com/problems/closest-prime-numbers-in-range)

### cpp
```cpp
class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> sieve(right + 1, true);
        sieve[0] = sieve[1] = false;

        for(int i=2; i*i <= right; ++i) {
            if(sieve[i])
                for(int j=i*i; j<=right; j+=i)
                    sieve[j] = false;
        }

        vector<int> ans = {-1, -1};
        int lastPrime=-1, maxGap = INT_MAX;
        for(int i=left; i<=right; ++i) {
            if(sieve[i]) {
                if(lastPrime != -1 && i-lastPrime<maxGap) {
                    maxGap = i-lastPrime;
                    ans = {lastPrime, i};
                }
                lastPrime = i;
            }
        }

        return ans;
    }
};
```
