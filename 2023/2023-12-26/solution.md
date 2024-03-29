# Solution - 26 Dec 2023

---
## [1155. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum)

### cpp
```cpp
#define MOD 1000000007

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        long long dp[31][1001] = {1};

        for(int i=1; i<=n; ++i) {
            for(int j=1; j <= min(target, i*k); ++j) {
                long long tmp = 0;
                for(int kk=j-1; kk >= max(0, j-k); --kk) 
                    tmp += dp[i-1][kk] % MOD;
                dp[i][j] =  tmp;
            }
        }

        return dp[n][target] % MOD;
    }
};
```
