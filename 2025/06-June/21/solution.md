# Solution - 21 Jun 2025

---
## [3085. Minimum Deletions to Make String K-Special](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special)

### cpp
```cpp
class Solution {
public:
    int minimumDeletions(string word, int k) {
        int cnt[26] = {0}, ans = word.size();

        for(char ch:word)
            cnt[ch-'a']++;

        for(int i=0; i<26; ++i) {
            int curr = 0;

            for(int j=0; j<26; ++j)
                curr += (cnt[j] < cnt[i]) ? cnt[j] : max(0, cnt[j] - (cnt[i] + k));

            ans = min(ans, curr);
        }

        return ans;
    }
};
```
