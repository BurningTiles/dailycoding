# Solution - 05 Jan 2024

---
## [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)

### cpp
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& A) {
        vector<int> v(A.size());
        v[0] = 1;
        int ans = 1;
        for(int i=1; i<A.size(); i++){
            v[i] = 1;
            for(int j=i-1; j>=0; j--)
                if(A[i]>A[j])
                    v[i] = max(v[i], v[j]+1);
            ans = max(v[i], ans);
        }
        return ans;
    }
};
```
