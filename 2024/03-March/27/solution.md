# Solution - 27 Mar 2024

---
## [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k)

### cpp
```cpp
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        long long product = 1, j = 0, ans = 0;
        
        for(int i=0; i<nums.size(); ++i) {
            product *= nums[i];

            while(j<=i && product >= k) 
                product /= nums[j++];
            
            ans += i-j+1;
        }

        return ans;
    }
};
```
