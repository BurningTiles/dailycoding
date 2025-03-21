# Solution - 10 Mar 2025

---
## [3306. Count of Substrings Containing Every Vowel and K Consonants II](https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii)

### cpp
```cpp
class Solution {
    const string vowels = "aeiou";

public:
    bool isVowel(char ch) { return vowels.find(ch) != -1; }

    long long countOfSubstrings(string word, int k) {
        unordered_map<char, int> umap;
        long long cnst = 0, ans = 0, n = word.size();

        vector<int> nextCnst(n);
        int lastCnst = n;
        for (int i = n - 1; i >= 0; i--) {
            nextCnst[i] = lastCnst;
            if (!isVowel(word[i]))
                lastCnst = i;
        }

        int left = 0, right = 0;
        while (right < n) {
            if (isVowel(word[right]))
                umap[word[right]]++;
            else
                cnst++;

            while (left <= right && cnst > k) {
                if (isVowel(word[left])) {
                    if (--umap[word[left]] == 0)
                        umap.erase(word[left]);
                } else
                    cnst--;
                left++;
            }

            while (left < right && umap.size() == 5 && cnst == k) {
                ans += (nextCnst[right] - right);
                if (isVowel(word[left])) {
                    if (--umap[word[left]] == 0)
                        umap.erase(word[left]);
                } else
                    cnst--;
                left++;
            }

            ++right;
        }

        return ans;
    }
};
```
