# Solution - 22 Jun 2025

---
## [2138. Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k)

### cpp
```cpp
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;

        for(int i=0; i<s.size(); i+=k)
            ans.push_back(s.substr(i, k));
        
        while(ans.back().size() < k)
            ans.back().push_back(fill);

        return ans;
    }
};
```
