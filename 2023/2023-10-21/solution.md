# Solution - 21 Oct 2023

---
## [1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum)

### cpp
```cpp
class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(false),cin.tie(0);
        deque<int> dq;
        int res=nums[0];
        for(int i=0; i<nums.size() ;i++){
            nums[i] += dq.size() ? dq.front() : 0;
            res = max(res, nums[i]);
            while(!dq.empty() && nums[i]>dq.back())
                dq.pop_back();
            if(i>=k && !dq.empty() && dq.front()==nums[i-k])
                dq.pop_front();
            if(nums[i]>0) dq.push_back(nums[i]);
        }
        return res;
    }
};



























```
