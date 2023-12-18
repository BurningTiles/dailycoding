# Solution - 18 Dec 2023

---
## [1913. Maximum Product Difference Between Two Pairs](https://leetcode.com/problems/maximum-product-difference-between-two-pairs)

### cpp
```cpp
class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int max1=INT_MIN, max2=INT_MIN, min1=INT_MAX, min2=INT_MAX;
        
        for(auto n:nums) {
            if(n > max1)
                max2 = max1, max1 = n;
            else if(n > max2)
                max2 = n;
            
            if(n < min1)
                min2 = min1, min1 = n;
            else if(n < min2)
                min2 = n;
        }

        return (max1*max2) - (min1*min2);
    }
};
```