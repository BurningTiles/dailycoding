# Solution - 29 Apr 2024

---
## [2997. Minimum Number of Operations to Make Array XOR Equal to K](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k)

### cpp
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int x = k, ans = 0;

        for(int i=0; i<nums.size(); ++i)
            x ^= nums[i];

        while(x) {
            if(x&1) ++ans;
            x >>= 1;
        }

        return ans;
    }
};
```
