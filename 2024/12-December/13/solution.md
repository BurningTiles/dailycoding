# Solution - 13 Dec 2024

---
## [2593. Find Score of an Array After Marking All Elements](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements)

### cpp
```cpp
class Solution {
public:
    long long findScore(vector<int>& nums) {
        long long ans = 0;
        set<pair<int, int>> st;

        for(int i=0; i<nums.size(); ++i)
            st.insert({nums[i], i});

        for(auto &p:st) {
            if(nums[p.second] == 0)
                continue;
            
            ans += p.first;
            nums[p.second] = 0;

            if(p.second - 1 >= 0)
                nums[p.second - 1] = 0;
            if(p.second + 1 < nums.size())
                nums[p.second + 1] = 0;
        }

        return ans;
    }
};
```
