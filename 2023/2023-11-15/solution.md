# Solution - 15 Nov 2023

---
## [1846. Maximum Element After Decreasing and Rearranging](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging)

### cpp
```cpp
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        int n = arr.size(), ans = 0;
        vector<int> cnt(n+1, 0);
        for(int i=0; i<n; i++) 
            arr[i]>n ? cnt[n]++ : cnt[arr[i]]++;

        for(int i=1; i<=n; i++)
            ans = min(i, ans + cnt[i]);

        return ans;
    }
};
```
