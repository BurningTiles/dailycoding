# Solution - 16 Mar 2024

---
## [525. Contiguous Array](https://leetcode.com/problems/contiguous-array)

### cpp
```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size(), sum = 0, ans = 0;
        unordered_map<int, int> um; um[0] = 1;

        for(int i=0; i<n; ++i) {
            sum += nums[i] ? 1 : -1;
            if(um[sum]) 
                ans = max(ans, i - um[sum] + 2);
            else 
                um[sum] = i+2;
        }
        
        return ans;
    }
};
```
