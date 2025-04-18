# Solution - 08 Jan 2025

---
## [3042. Count Prefix and Suffix Pairs I](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i)

### cpp
```cpp
class Solution {
public:
    bool isPrefixAndSuffix(string &s1, string &s2) {
        if(s1.size() > s2.size()) return false;
        int i=0, n1=s1.size(), n2=s2.size();

        while(i<n1) {
            if(s1[i] != s2[i]) return false;
            if(s1[n1-i-1] != s2[n2-i-1]) return false;
            ++i;
        }

        return true;
    }

    int countPrefixSuffixPairs(vector<string>& words) {
        int ans = 0;

        for(int i=0; i<words.size(); ++i)
            for(int j=i+1; j<words.size(); ++j)
                ans += isPrefixAndSuffix(words[i], words[j]);
        
        return ans;
    }
};
```
