# Solution - 23 Apr 2025

---
## [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group)

### cpp
```cpp
class Solution {
public:
    int sumOfDigits(int val) {
        int ans = 0;
        while(val) {
            ans += val%10;
            val /= 10;
        }
        return ans;
    }

    int countLargestGroup(int n) {
        int counts[37] = {0}, maxLen = 0, ans = 0;

        for(int i=1; i<=n; ++i)
            ++counts[sumOfDigits(i)];

        for(int count:counts) {
            if(count > maxLen)
                maxLen = count, ans = 1;
            else if(count == maxLen)
                ++ans;
        }

        return ans;
    }
};
```
