# Solution - 04 Nov 2024

---
## [3163. String Compression III](https://leetcode.com/problems/string-compression-iii)

### cpp
```cpp
class Solution {
public:
    string compressedString(string word) {
        string ans = "";
        int cnt = 1;
        char last = word[0];

        for (int i = 1; i < word.size(); ++i) {
            if (word[i] == last && cnt < 9)
                ++cnt;
            else {
                ans.push_back(cnt + '0');
                ans.push_back(last);
                last = word[i];
                cnt = 1;
            }
        }
        ans.push_back(cnt + '0');
        ans.push_back(last);

        return ans;
    }
};
```
