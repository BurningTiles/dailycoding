# Solution - 04 Aug 2024

---
## [1508. Range Sum of Sorted Subarray Sums](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums)

### cpp
```cpp
class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        vector<long long> v;
        
        for(int i=0; i<nums.size(); ++i) {
            long long sum = 0;
            for(int j=i; j<nums.size(); ++j) {
                sum += nums[j];
                v.push_back(sum);
            }
        }

        sort(v.begin(), v.end());

        long long ans = 0;
        for(int i=left-1; i<right; ++i)
            ans += v[i], ans %= 1000000007;
        
        return ans;
    }
};
```
