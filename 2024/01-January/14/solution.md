# Solution - 14 Jan 2024

---
## [1657. Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close)

### cpp
```cpp
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if(word1.size() != word2.size()) return false;
        int cnt1[128] = {0}, cnt2[128] = {0};

        for(int i=0; i<word1.size(); ++i)
            cnt1[word1[i]]++, cnt2[word2[i]]++;

        vector<int> v1, v2;
        
        for(int i=97; i<124; ++i)
            if(cnt1[i] != cnt2[i]) {
                if(cnt1[i]==0 || cnt2[i]==0)
                    return false;
                v1.push_back(cnt1[i]);
                v2.push_back(cnt2[i]);
            }
        
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());

        return v1==v2;
    }
};
```
