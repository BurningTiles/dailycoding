# Solution - 28 Jun 2025

---
## [2099. Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum)

### cpp
```cpp
class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<pair<int, int>> v;

        for(int i=0; i<nums.size(); ++i)
            v.push_back({nums[i], i});

        sort(v.begin(), v.end());
        sort(v.begin()+(nums.size() - k), v.end(), [](pair<int, int> a, pair<int, int> b){ return a.second<b.second;});

        vector<int> ans;

        for(int i=nums.size()-k; i<nums.size(); ++i)
            ans.push_back(v[i].first);

        return ans;
    }
};
```
