# Solution - 17 Apr 2025

---
## [2176. Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array)

### cpp
```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> umap;
        int ans = 0;

        for(int i=0; i<nums.size(); ++i) {
            for(int j:umap[nums[i]])
                if((i * j) % k == 0)
                    ++ans;

            umap[nums[i]].push_back(i);
        }

        return ans;
    }
};
```
