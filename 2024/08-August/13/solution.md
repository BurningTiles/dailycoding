# Solution - 13 Aug 2024

---
## [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii)

### cpp
```cpp
class Solution {
public:
    void helper(vector<int> &A, vector<vector<int>> &ans, vector<int> &cur, int target, int i=0) {
        if(target==0) { ans.push_back(cur); return; }
        for(int j=i; j<A.size(); j++) {
            if(A[j]>target || (j>i && A[j]==A[j-1])) continue;
            cur.push_back(A[j]);
            helper(A, ans, cur, target-A[j], j+1);
            cur.pop_back();
        }
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> cur;
        
        helper(candidates, ans, cur, target);
        return ans;
    }
};
```
