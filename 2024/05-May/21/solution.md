# Solution - 21 May 2024

---
## [78. Subsets](https://leetcode.com/problems/subsets)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;

        for(int i=0; i<1<<nums.size(); ++i) {
            vector<int> subset;
            for(int j=0, x=i; j<11 && x; ++j, x/=2)
                if(x&1)
                    subset.push_back(nums[j]);
            
            ans.push_back(subset);
        }

        return ans;
    }
};
```
