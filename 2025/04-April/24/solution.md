# Solution - 24 Apr 2025

---
## [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array)

### cpp
```cpp
class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        unordered_map<int, int> umap;

        for(int num:nums)
            umap[num]++;

        int unique = umap.size(), ans = 0, n = nums.size();
        umap.clear();

        for(int i=0, j=0; i<n; ++i) {
            while(j<n && umap.size() < unique) {
                umap[nums[j]]++;
                ++j;
            }

            if(umap.size() == unique)
                ans += n - j + 1;
            
            if((--umap[nums[i]]) == 0) {
                umap.erase(nums[i]);
            }
        }

        return ans;
    }

    /*
    int countCompleteSubarrays(vector<int>& nums) {
        unordered_map<int, int> umap;

        for(int num:nums)
            umap[num]++;

        int unique = umap.size(), ans = 0, n = nums.size();

        for(int i=0; i<n; ++i) {
            umap.clear();
            for(int j=i; j<n; ++j) {
                umap[nums[j]]++;
                if(umap.size() == unique) {
                    ans += n - j;
                    break;
                }
            }
        }

        return ans;
    }
    */
};
```
