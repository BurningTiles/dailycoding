# Solution - 10 Mar 2024

---
## [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays)

### cpp
```cpp
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> count;
        vector<int> ans;

        for(auto num:nums1) count[num]++;
        for(auto num:nums2)
            if(count[num])
                ans.push_back(num), count[num] = 0;

        return ans;
    }
};
```
