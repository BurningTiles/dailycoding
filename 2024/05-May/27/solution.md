# Solution - 27 May 2024

---
## [1608. Special Array With X Elements Greater Than or Equal X](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x)

### cpp
```cpp
class Solution {
public:
    int specialArray(vector<int>& nums) {
        int cnt[102] = {0}, n = nums.size();
        
        for(int num:nums) 
            cnt[min(num, n)]++;
        
        for(int i=n; i>=0; --i) {
            cnt[i] = cnt[i+1] + cnt[i];
            if (cnt[i] == i)
                return i;
        }

        return -1;
    }
};
```
