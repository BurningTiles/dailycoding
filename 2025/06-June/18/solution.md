# Solution - 18 Jun 2025

---
## [2966. Divide Array Into Arrays With Max Difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference)

### cpp
```cpp
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int n = nums.size();
        vector<vector<int>> ans;

        for(int i=0; i<n; i+=3) {
            if(nums[i+2]-nums[i] > k)
                return {};
            ans.push_back({nums[i], nums[i+1], nums[i+2]});
        }

        return ans;
    }
};
```
