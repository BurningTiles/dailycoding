# Solution - 15 Mar 2024

---
## [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)

### cpp
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(), tmp = 1;
        vector<int> ans(n+1);
        ans[0] = 1;
        for(int i=1; i<=n; ++i)
            ans[i] = ans[i-1] * nums[i-1];
        
        for(int i=n-1; i>=0; --i)
            ans[i] *= tmp,
            tmp *= nums[i];
        
        ans.pop_back();
        return ans;
    }
};
```
