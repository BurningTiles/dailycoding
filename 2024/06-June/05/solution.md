# Solution - 05 Jun 2024

---
## [1002. Find Common Characters](https://leetcode.com/problems/find-common-characters)

### cpp
```cpp
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> cnt(26, INT_MAX);
        
        for(int i=0; i<words.size(); ++i) {
            int curCnt[26] = {0};

            for(auto ch:words[i]) 
                ++curCnt[ch - 'a'];
            for(auto i=0; i<26; ++i)
                cnt[i] = min(cnt[i], curCnt[i]);
        }

        vector<string> ans;
        for(int i=0; i<26; ++i)
            while(cnt[i]--) ans.push_back(string(1, i+'a'));
        
        return ans;
    }
};
```
