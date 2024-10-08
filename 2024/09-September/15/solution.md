# Solution - 15 Sep 2024

---
## [1371. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts)

### cpp
```cpp
class Solution {
public:
    int findTheLongestSubstring(string s) {
        unordered_map<int, int> m;
        m[0] = -1;
        string vovels = "aeiou";
        int mask = 0, ans = 0;

        for(int i=0; i<s.size(); ++i) {
            for(int j=0; j<5; ++j) {
                if(s[i] == vovels[j]) {
                    mask ^= (1 << j);
                    break;
                }
            }

            if(m.find(mask) == m.end())
                m[mask] = i;
            
            ans = max(ans, i - m[mask]);
        }

        return ans;
    }
};
```
