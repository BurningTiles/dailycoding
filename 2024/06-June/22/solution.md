# Solution - 22 Jun 2024

---
## [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays)

### cpp
```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        int ans = 0, j = 0, cnt = 1;
        
        for(int i=0; i<nums.size(); ++i) {
            if(nums[i]&1) --k;
            if(k < 0)
                ++j, cnt = 1, ++k;

            while(j<=i && !(nums[j]&1))
                ++cnt, ++j;

            if(!k) ans += cnt;
        }

        return ans;
    }
};
```
