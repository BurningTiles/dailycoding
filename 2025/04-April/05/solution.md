# Solution - 05 Apr 2025

---
## [1863. Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals)

### cpp
```cpp
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int ans = 0;
        dfs(nums, ans);
        return ans;
    }

    void dfs(vector<int> &nums, int &ans, int cur=0, int i=0) {
        if(i==nums.size()) {
            ans += cur;
            return;
        }
        dfs(nums, ans, cur, i+1);
        dfs(nums, ans, cur^nums[i], i+1);
    }
};
```
