# Solution - 02 Sep 2024

---
## [1894. Find the Student that Will Replace the Chalk](https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk)

### cpp
```cpp
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        long long sum = 0;

        for(int i=0; i<chalk.size(); ++i)
            sum += chalk[i];
        
        k %= sum;

        for(int i=0; i<chalk.size(); ++i) {
            if(chalk[i]>k) return i;
            k -= chalk[i];
        }

        return 0;
    }
};
```
