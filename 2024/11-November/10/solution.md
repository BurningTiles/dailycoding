# Solution - 10 Nov 2024

---
## [3097. Shortest Subarray With OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii)

### cpp
```cpp
class Solution {
public:
    void addOr(vector<int> &bitCnt, int &orVal, int n) {
        orVal = (orVal | n);
        for(int i=0; i<32 && n; ++i, n/=2)
            bitCnt[i] += n&1;
    }

    void removeOr(vector<int> &bitCnt, int &orVal, int n) {
        for(int i=0; i<32 && n; ++i, n/=2) {
            bitCnt[i] -= n&1;
            if(bitCnt[i] == 0)
                orVal = orVal & (~(1<<i));
        }
    }

    int minimumSubarrayLength(vector<int>& nums, int k) {
        int orVal = 0, ans = INT_MAX;
        vector<int> bitCnt(32, 0);
        
        for(int i=0, j=0; i<nums.size(); ++i) {
            addOr(bitCnt, orVal, nums[i]);
            if(orVal < k) continue;
            
            for(; j<=i && orVal >= k; ++j) {
                removeOr(bitCnt, orVal, nums[j]);
                ans = min(ans, i - j + 1);
            }
        }

        return ans == INT_MAX ? -1 : ans;
    }
};
```
