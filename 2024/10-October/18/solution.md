# Solution - 18 Oct 2024

---
## [2044. Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets)

### cpp
```cpp
class Solution {
public:
    void backtrack(vector<int> &nums, int index, int curxor, int maxor, int &ans) {
        if(curxor == maxor)
            ++ans;
        
        for(int i=index; i<nums.size(); ++i)
            backtrack(nums, i+1, curxor | nums[i], maxor, ans);
    }

    int countMaxOrSubsets(vector<int>& nums) {
        int maxor = 0, ans = 0;

        for(int num:nums)
            maxor |= num;
        
        backtrack(nums, 0, 0, maxor, ans);

        return ans;
    }
};
```
