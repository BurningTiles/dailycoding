# Solution - 02 Jan 2024

---
## [2610. Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<vector<int>> ans;
    
        sort(nums.begin(), nums.end());
        for(int i=0, cnt=1; i<nums.size(); ++i) {
            if(i && nums[i]==nums[i-1]) ++cnt;
            else cnt = 1;
            
            if(cnt > ans.size()) 
                ans.push_back({nums[i]});
            else 
                ans[cnt-1].push_back(nums[i]);
        }

        return ans;
    }
};
```
