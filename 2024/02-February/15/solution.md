# Solution - 15 Feb 2024

---
## [2971. Find Polygon With the Largest Perimeter](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter)

### cpp
```cpp
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        long long sum = nums[0], ans = -1;

        for(int i=1; i<nums.size()-1; ++i) {
            sum += nums[i];
            if(sum > nums[i+1])
                ans = sum + nums[i+1];
        }

        return ans;
    }
};
```
