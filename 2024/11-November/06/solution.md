# Solution - 06 Nov 2024

---
## [3011. Find if Array Can Be Sorted](https://leetcode.com/problems/find-if-array-can-be-sorted)

### cpp
```cpp
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        int start = 0, bits = 0;
        
        for(int i=0; i<nums.size(); ++i) {
            int tmp = nums[i], curBits = 0;
            while(tmp) {
                curBits += tmp&1;
                tmp /= 2;
            }
            if(bits != curBits) {
                if(i>0) {
                    sort(nums.begin()+start, nums.begin() + i);
                    start = i;
                }
                bits = curBits;
            }
        }

        sort(nums.begin()+start, nums.end());

        for(int i=1; i<nums.size(); ++i)
            if(nums[i] < nums[i-1])
                return false;
        
        return true;
    }
};
```
