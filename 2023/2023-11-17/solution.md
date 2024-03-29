# Solution - 17 Nov 2023

---
## [1877. Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array)

### cpp
```cpp
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
        
        int cnt[100001] = {0}, ans = 0, i=0, j=100000;
        
        for(int i=0; i<nums.size(); ++i)
            ++cnt[nums[i]];
        
        while(i<=j) {
            if(!cnt[i]) ++i;
            else if(!cnt[j]) --j;
            else {
                if(i+j > ans) ans = i+j;
                --cnt[i], --cnt[j];
            }
        }

        return ans;
    }
};
```
