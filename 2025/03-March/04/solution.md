# Solution - 04 Mar 2025

---
## [1780. Check if Number is a Sum of Powers of Three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three)

### cpp
```cpp
class Solution {
public:
    bool checkPowersOfThree(int n) {
        if(n%3 == 2) return false;
        vector<long long> p3 = {1};
        for(int i=1; i<17; ++i)
            p3.push_back(p3.back()*3);
        
        for(int i=16; i>=0; --i)
            if(n >= p3[i]) n -= p3[i];
        
        return n == 0;
    }
};
```
