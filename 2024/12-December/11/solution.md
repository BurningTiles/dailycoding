# Solution - 11 Dec 2024

---
## [2779. Maximum Beauty of an Array After Applying Operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation)

### cpp
```cpp
class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int start = 0, ans = 0;

        for(int i=0; i<nums.size(); ++i) {
            while(nums[i]-nums[start] > 2*k)
                ++start;
            ans = max(ans, i-start+1);
        }

        return ans;
    }
};
```
