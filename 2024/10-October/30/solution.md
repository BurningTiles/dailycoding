# Solution - 30 Oct 2024

---
## [1671. Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array)

### cpp
```cpp
class Solution {
public:
    vector<int> longestInc(vector<int> &v) {
        vector<int> lst = {v[0]};
        vector<int> ans(v.size(), 1);

        for(int i=1; i<v.size(); ++i) {
            if(v[i] > lst.back())
                lst.push_back(v[i]);
            else {
                int index = lower_bound(lst.begin(), lst.end(), v[i]) - lst.begin();
                lst[index] = v[i];
            }
            ans[i] = lst.size();
        }

        return ans;
    }

    int minimumMountainRemovals(vector<int>& nums) {
        int n = nums.size();
        vector<int> lstInc = longestInc(nums);

        reverse(nums.begin(), nums.end());
        vector<int> lstDec = longestInc(nums);
        reverse(lstDec.begin(), lstDec.end());

        int ans = INT_MAX; // Number of items need to be removed.

        for(int i=0; i<n; ++i)
            if(lstInc[i] > 1 && lstDec[i] > 1)
                ans = min(ans, n + 1 - (lstInc[i] + lstDec[i]));
        
        return ans;
    }
};
```
