# Solution - 13 Sep 2024

---
## [1310. XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray)

### cpp
```cpp
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> ans(queries.size()), com(arr.size()+1, 0);

        for(int i=0; i<arr.size(); ++i)
            com[i+1] = com[i] ^ arr[i];

        for(int i=0; i<queries.size(); ++i)
            ans[i] = com[queries[i][0]] ^ com[queries[i][1]+1];

        return ans;
    }
};
```
