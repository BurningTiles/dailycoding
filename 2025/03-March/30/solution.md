# Solution - 30 Mar 2025

---
## [763. Partition Labels](https://leetcode.com/problems/partition-labels)

### cpp
```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        int last[128] = {-1};

        for(int i=0; i<s.size(); ++i)
            last[s[i]] = i;
        
        vector<int> ans;
        int i=0, j=0, len=0;

        do {
            j = max(j, last[s[i]]);
            ++len;
            if(i == j) {
                ans.push_back(len);
                len = 0;
            }
            ++i;
        } while(i<s.size());

        return ans;
    }
};
```
