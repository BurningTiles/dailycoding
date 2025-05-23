# Solution - 22 May 2025

---
## [3362. Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii)

### cpp
```cpp
class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), nq = queries.size();
        sort(queries.begin(), queries.end());

        priority_queue<int> h; // max heap
        vector<int> end(n+1, 0);

        int cur = 0, j = 0;
        for(int i=0; i<n; ++i) {
            cur -= end[i];
            while(j < nq && queries[j][0] <= i) {
                h.push(queries[j][1]);
                ++j;
            }
            while(cur < nums[i]) {
                if(h.empty() || h.top() < i)
                    return -1;
                end[h.top() + 1]++;
                h.pop();
                ++cur;
            }
        }

        return h.size();
    }
};
```
