# Solution - 05 Oct 2024

---
## [567. Permutation in String](https://leetcode.com/problems/permutation-in-string)

### cpp
```cpp
class Solution {
public:
    bool isPermute(int *cnt1, int *cnt2) {
        for(int i=97; i<123; ++i)
            if(cnt1[i] != cnt2[i])
                return false;
        return true;
    }

    bool checkInclusion(string s1, string s2) {
        if(s2.size() < s1.size())
            return false;

        int cnt1[128] = {0}, cnt2[128] = {0}, l1=s1.size(), l2=s2.size();

        for(int i=0; i<l1-1; ++i)
            cnt1[s1[i]]++, cnt2[s2[i]]++;
        cnt1[s1.back()]++;
        
        for(int i=l1-1; i<l2; ++i) {
            cnt2[s2[i]]++;
            if(isPermute(cnt1, cnt2))
                return true;
            
            cnt2[s2[i-l1+1]]--;
        }

        return false;
    }
};
```
