# Solution - 09 May 2024

---
## [3075. Maximize Happiness of Selected Children](https://leetcode.com/problems/maximize-happiness-of-selected-children)

### cpp
```cpp
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>());
        long long ans = 0;

        for(int i=0; i<k && i<happiness.size(); ++i)
            ans += max(happiness[i]-i, 0);

        return ans;
    }
};
```
