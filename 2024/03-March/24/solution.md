# Solution - 24 Mar 2024

---
## [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)

### cpp
```cpp
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0], fast = nums[slow];

        while(slow != fast)
            slow = nums[slow],
            fast = nums[nums[fast]];
        
        slow = 0;
        
        while(slow != fast)
            slow = nums[slow],
            fast = nums[fast];
        
        return fast;
    }
};
```
