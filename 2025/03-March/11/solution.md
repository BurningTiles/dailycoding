# Solution - 11 Mar 2025

---
## [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters)

### cpp
```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        int ans = 0, i=0, j=0, x[128]={0};
        x[s[0]]++;
        while(j<s.size()){
            if(x[97] && x[98] && x[99]){
                ans += s.size()-j;
                x[s[i]]--;
                i++;
            }
            else{
                j++;
                x[s[j]]++;
            }
        }
        return ans;
    }
};
```
