# Solution - 02 Jul 2024

---
## [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii)

### cpp
```cpp
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> um;
        vector<int> ans;

        for(int i=0; i<nums1.size(); ++i)
            um[nums1[i]]++;
        
        for(int i=0; i<nums2.size(); ++i)
            if(um[nums2[i]])
                um[nums2[i]]--, ans.push_back(nums2[i]);
        
        return ans;
    }
};
```
