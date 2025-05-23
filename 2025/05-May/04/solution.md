# Solution - 04 May 2025

---
## [1128. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs)

### cpp
```cpp
class Solution {
public:
    uint64_t key(int a, int b) {
        return (uint64_t) a << 32 | b; 
    }

    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<uint64_t, int> umap;
        int ans = 0;

        for(auto &d:dominoes) {
            int a = d[0], b = d[1];
            if(b > a)
                swap(a, b);
            ans += umap[key(a, b)]++;
        }

        return ans;
    }
};
```
