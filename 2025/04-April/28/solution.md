# Solution - 28 Apr 2025

---
## [2302. Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k)

### cpp
```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        long long ans = 0, sum = 0;

        for(int i=0, j=0; i<nums.size(); ++i) {
            sum += nums[i];

            while(sum * (i-j+1) >= k)
                sum -= nums[j++];
            
            ans += i - j + 1;
        }

        return ans;
    }
};
```
