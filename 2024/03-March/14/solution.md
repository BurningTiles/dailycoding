# Solution - 14 Mar 2024

---
## [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum)

### cpp
```cpp
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int i = 0, count = 0, ans = 0;
        
        for(int j=0; j<nums.size(); ++j) {
            if(nums[j]) --goal, count = 0;

            while(goal == 0 && i<=j) {
                goal += nums[i++];
                ++count;
                if (i > j-goal+1) 
                    break;
            }

            while(goal < 0)
                goal += nums[i++];
            
            ans += count;
        }

        return ans;
    }
};
```
