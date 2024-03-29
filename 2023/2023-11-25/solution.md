# Solution - 25 Nov 2023

---
## [1685. Sum of Absolute Differences in a Sorted Array](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array)

### cpp
```cpp
auto init = [](){ios::sync_with_stdio(0); cin.tie(0); cout.tie(0); return 0;}();

class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        long long n = nums.size(), leftSum = 0, rightSum = 0;
        for(int i=0; i<n; ++i) rightSum += nums[i];

        for(int i=0; i<n; ++i) {
            int tmp = nums[i]*i - leftSum + rightSum - nums[i]*(n-i);
            leftSum += nums[i], rightSum -= nums[i], nums[i] = tmp;
        }
        
        return nums;
    }
};
```
