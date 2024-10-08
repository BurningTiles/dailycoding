# Solution - 25 Sep 2024

---
## [2416. Sum of Prefix Scores of Strings](https://leetcode.com/problems/sum-of-prefix-scores-of-strings)

### cpp
```cpp
struct Trie {
    Trie* next[26];
    int count;
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie* trie = new Trie();
        vector<int> ans;

        for (auto& word : words) {
            Trie* ptr = trie;
            for (char ch : word) {
                if (!ptr->next[ch - 'a'])
                    ptr->next[ch - 'a'] = new Trie();
                ptr = ptr->next[ch - 'a'];
                ptr->count++;
            }
        }

        for (auto& word : words) {
            Trie* ptr = trie;
            int score = 0;
            for (char ch : word) {
                ptr = ptr->next[ch - 'a'];
                score += ptr->count;
            }
            ans.push_back(score);
        }

        return ans;
    }
};
```
