# Solution - 14 Feb 2024

---
## [2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign)

### cpp
```cpp
class Solution {
public:
    Solution() {ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);}

    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> ans(nums.size());
        
        for(int i=0, j=1, x=0; x<nums.size(); ++x)
            if(nums[x] > 0) ans[i] = nums[x], i += 2;
            else ans[j] = nums[x], j += 2;
        
        return ans;
    }
};
```
