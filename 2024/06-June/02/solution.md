# Solution - 02 Jun 2024

---
## [344. Reverse String](https://leetcode.com/problems/reverse-string)

### cpp
```cpp
class Solution {
public:
    void reverseString(vector<char>& s) {
        for(int i=0, j=s.size()-1; i<j; ++i,--j)
            swap(s[i], s[j]);
    }
};
```
