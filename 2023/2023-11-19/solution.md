# Solution - 19 Nov 2023

---
## [1887. Reduction Operations to Make the Array Elements Equal](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal)

### cpp
```cpp
class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        int cnt[50001] = {0}, n = nums.size(), ans = 0, op = 0;
        for(int i=0; i<n; ++i)
            ++cnt[nums[i]];
        
        for(int i=50000; i>0; --i)
            if(cnt[i]) {
                ans += op;
                op += cnt[i];
            }
        
        return ans;
    }
};
```
