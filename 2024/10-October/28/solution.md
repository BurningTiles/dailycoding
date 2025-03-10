# Solution - 28 Oct 2024

---
## [2501. Longest Square Streak in an Array](https://leetcode.com/problems/longest-square-streak-in-an-array)

### cpp
```cpp
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        int ans = 0;
        unordered_map<int, int> umap;

        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size(); ++i) {
            int x = sqrt(nums[i]);
            
            if(nums[i] == x*x)
                umap[nums[i]] = umap[x] + 1;
            else
                umap[nums[i]] = 1;

            ans = max(ans, umap[nums[i]]);
        }

        return ans>1 ? ans : -1;
    }
};
```
