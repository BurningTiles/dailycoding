# Solution - 16 Nov 2024

---
## [3254. Find the Power of K-Size Subarrays I](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i)

### cpp
```cpp
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        int n = nums.size(), score = 0;
        vector<int> ans(n-k+1, -1);
        
        for(int i=0; i<nums.size(); ++i) {
            if(i && nums[i-1] + 1 == nums[i])
                score++;
            else
                score = 0;
            if(score >= k-1)
                ans[i-k+1] = nums[i];
        }

        return ans;
    }
};
```
