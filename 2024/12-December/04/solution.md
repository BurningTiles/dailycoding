# Solution - 04 Dec 2024

---
## [2825. Make String a Subsequence Using Cyclic Increments](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments)

### cpp
```cpp
class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int i=0, j=0;

        while(j<str2.size()) {
            int ch1 = str2[j], ch2 = (ch1 == 97 ? 122 : ch1-1);
            
            while(i<str1.size()) {
                if(str1[i] == ch1 || str1[i] == ch2)
                    break;
                ++i;
            }
            
            if(i == str1.size())
                return false;
            ++i,++j;
        }

        return true;
    }
};
```
