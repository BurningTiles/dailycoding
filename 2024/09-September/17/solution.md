# Solution - 17 Sep 2024

---
## [884. Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences)

### cpp
```cpp
class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> um;
        vector<string> ans;

        stringstream ss(s1 + " " + s2);
        
        while(ss >> s1)
            um[s1]++;
        
        for(auto p:um)
            if(p.second == 1)
                ans.push_back(p.first);
        
        return ans;
    }
};
```
