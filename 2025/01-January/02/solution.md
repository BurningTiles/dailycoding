# Solution - 02 Jan 2025

---
## [2559. Count Vowel Strings in Ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges)

### cpp
```cpp
class Solution {
public:
    bool isVowel(char c){ 
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' ||  c == 'u';
    }

    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        vector<int> v, ans;
        v.push_back(0);

        for(auto w: words){ 
            if(isVowel(w[0]) && isVowel(w.back())) 
                v.push_back(v.back() + 1);  
            else 
                v.push_back(v.back());
        }

        for(auto q: queries) 
            ans.push_back(v[q[1]+1] - v[q[0]]);
            
        return ans;
    }
};
```
