# Solution - 07 Feb 2024

---
## [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency)

### cpp
```cpp
class Solution {
public:
    string frequencySort(string s) {
        pair<int, char> count[128] = {{0, 0}};

        for(auto ch:s) count[ch].first--, count[ch].second = ch;
        sort(count, count+128);

        string ans = "";
        for(auto &p:count)
            while(p.first++) ans.push_back(p.second);
        
        return ans;
    }
};
```
