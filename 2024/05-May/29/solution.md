# Solution - 29 May 2024

---
## [1404. Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one)

### cpp
```cpp
class Solution {
public:
    int numSteps(string s) {
        int ones = 0, last_one = 0;
        
        for(int i=1; i<s.size(); ++i)
            if(s[i] == '1')
                last_one = i, ++ones;
        
        return s.size()-1 + (last_one - ones) + (last_one ? 2 : 0);
    }
};
```
