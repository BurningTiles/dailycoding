# Solution - 28 Dec 2024

---
## [689. Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays)

### cpp
```cpp
class Solution {
public:
    vector<int> maxSumOfThreeSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> sums;

        for(int i=0, sum=0; i<nums.size(); ++i) {
            sum += nums[i];
            if(i >= k) sum -= nums[i-k];
            if(i >= k-1) sums.push_back(sum);
        }

        int ss = sums.size();
        vector<int> left(ss), right(ss);

        for(int i=0, best=0; i<ss; ++i){
            if(sums[i] > sums[best]) best = i;
            left[i] = best;
        }

        for(int i=ss-1, best=ss-1; i>=0; --i){
            if(sums[i] >= sums[best]) best = i;
            right[i] = best;
        }

        vector<int> ans;
        int totalSum = 0;
        for(int i=k; i<sums.size()-k; ++i) {
            int l = left[i-k], r = right[i+k];
            int tmp = sums[l] + sums[i] + sums[r];
            
            if(tmp > totalSum)
                ans = {l, i, r}, totalSum = tmp;
        }

        return ans;
    }
};
```
