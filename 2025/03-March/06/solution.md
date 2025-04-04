# Solution - 06 Mar 2025

---
## [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values)

### cpp
```cpp
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        long long n = grid.size(), n2 = n*n;

        long long exp_sum = n2 * (n2 + 1) / 2;
        long long exp_sum_square = n2 * (n2 + 1) * (2*n2 + 1) / 6;

        long long act_sum = 0, act_sum_square = 0;

        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                act_sum += grid[i][j], act_sum_square += grid[i][j] * grid[i][j];
            
        long long diff_sum = act_sum - exp_sum;
        long long diff_sum_square = act_sum_square - exp_sum_square;

        long long sum_a_b = diff_sum_square / diff_sum;

        int a = (sum_a_b + diff_sum) / 2;
        int b = (sum_a_b - diff_sum) / 2;

        return {a, b};
    }
};
```
