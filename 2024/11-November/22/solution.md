# Solution - 22 Nov 2024

---
## [1072. Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows)

### cpp
```cpp
class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        unordered_map<string, int> count;
        int ans = 0;

        for(auto &row:matrix) {
            string s="";

            for(int i=0; i<row.size(); ++i)
                s.push_back(row[i] == row[0] ? '0' : '1');

            count[s]++;
            ans = max(ans, count[s]);
        }

        return ans;
    }
};
```
