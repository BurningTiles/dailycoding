# Solution - 12 Sep 2024

---
## [1684. Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings)

### cpp
```cpp
class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int cnt[26] = {0}, ans = 0;
        for(int i=0; i<allowed.size(); ++i)
            cnt[allowed[i]-'a']++;

        for(auto &word:words) {
            bool flag = true;

            for(int i=0; i<word.size(); ++i)
                if(!cnt[word[i]-'a']) {
                    flag = false;
                    break;
                }
            
            if(flag) ++ans;
        }

        return ans;
    }
};
```
