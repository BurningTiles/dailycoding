# Solution - 24 Jun 2025

---
## [2200. Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array)

### cpp
```cpp
class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == key) {
                int j = 1;
                while (j<=k && i-j >= 0 && nums[i-j] != -1)
                    nums[i-j] = -1, ++j;

                j = 1;
                while (j<=k && i+j < nums.size() && nums[i+j] != key)
                    nums[i+j] = -1, ++j;

                nums[i] = -1;
            }
        }

        for (int i = 0; i < nums.size(); ++i)
            if (nums[i] == -1)
                ans.push_back(i);

        return ans;
    }
};
```
