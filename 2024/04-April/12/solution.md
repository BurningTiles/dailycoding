# Solution - 12 Apr 2024

---
## [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)

### cpp
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int i=0, j=height.size()-1, ml=0, mr=0, ans=0;

        while(i<=j) {
            ml = max(ml, height[i]);
            mr = max(mr, height[j]);

            ans += ml<mr ? ml-height[i++] : mr-height[j--];
        }

        return ans;
    }
};
```
