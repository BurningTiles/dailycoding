# Solution - 31 Dec 2023

---
## [1624. Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters)

### cpp
```cpp
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int index[128] = {0}, ans = -1;

        for(int i=0; i<s.size(); ++i)
            if(index[s[i]]==0) index[s[i]]=i+1;
            else ans = max(ans, i-index[s[i]]);

        return ans;
    }
};
```
