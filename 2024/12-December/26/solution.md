# Solution - 26 Dec 2024

---
## [494. Target Sum](https://leetcode.com/problems/target-sum)

### cpp
```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if(target > sum || target < -sum) return 0;

        vector<int> cur(2*sum+1), next(2*sum+1), *ptr1=&cur, *ptr2=&next;
        cur[sum] = 1;

        for(int i=0; i<nums.size(); ++i) {
            for(int j=0; j<=2*sum; ++j) {
                if(ptr1->at(j)) {
                    ptr2->at(j+nums[i]) += ptr1->at(j);
                    ptr2->at(j-nums[i]) += ptr1->at(j);
                }
            }
            swap(ptr1, ptr2);
            ptr2->assign(2*sum+1, 0);
        }

        return ptr1->at(target+sum);
    }
};
```
