# Solution - 13 Feb 2024

---
## [2108. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array)

### cpp
```cpp
class Solution {
public:
    Solution() {ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);}

    string firstPalindrome(vector<string>& words) {
        for(auto &word:words) {
            bool palindromic = true;
            for(int i=0, j=word.size()-1; i<j; ++i,--j)
                if(word[i] != word[j]) {
                    palindromic = false; break;
                }
            if (palindromic) return word;
        }

        return "";
    }
};
```
