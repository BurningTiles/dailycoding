# Solution - 12 Feb 2024

---
## [169. Majority Element](https://leetcode.com/problems/majority-element)

### cpp
```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count=0, ans=0;
        for(int i=0; i<nums.size(); i++) {
            if(!count)
                ans = nums[i];
            count += nums[i]==ans ? 1 : -1;
        }
        return ans;
    }
};
```
