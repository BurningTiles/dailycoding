# Solution - 03 Sep 2024

---
## [1945. Sum of Digits of String After Convert](https://leetcode.com/problems/sum-of-digits-of-string-after-convert)

### cpp
```cpp
class Solution {
public:
    int getLucky(string s, int k) {
        string num="";
        for(int i=0; i<s.size(); ++i)
            num += to_string(s[i]-'a'+1);
        
        for(int i=0; i<k; ++i) {
            int tmp = 0;
            for(int i=0; i<num.size(); ++i)
                tmp += num[i]-'0';
            num = to_string(tmp);
        }

        return stoi(num);
    }
};
```
