# Solution - 13 Nov 2024

---
## [2563. Count the Number of Fair Pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs)

### cpp
```cpp
class Solution {
public:
    long long countLess(vector<int>& nums, int val) {
        long long ans = 0;
        for (int i=0, j=nums.size()-1; i<j; ++i) {
            while (i<j && nums[i]+nums[j] > val)
                --j;
            ans += j-i;
        }
        return ans;
    }

    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        sort(begin(nums), end(nums));
        return countLess(nums, upper) - countLess(nums, lower - 1);
    }

    /*
    // Solution using binary search
    long long countFairPairs(vector<int>& nums, int lower, int upper) {
        long long ans = 0;
        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size()-1; ++i) {
            auto start = lower_bound(nums.begin() + i + 1, nums.end(), lower - nums[i]);
            auto end = upper_bound(nums.begin() + i + 1, nums.end(), upper - nums[i]);

            ans += end - start;
        }

        return ans;
    }
    */
};
```
