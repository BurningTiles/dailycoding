# Solution - 24 Aug 2024

---
## [564. Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome)

### cpp
```cpp
class Solution {
public:
    string nearestPalindromic(string n) {
        int size = n.size();
        set<long> nums;

        nums.insert(long(pow(10, size)) + 1);
        nums.insert(long(pow(10, size-1)) - 1);

        long prefix = stol(n.substr(0, (size + 1) / 2));

        for(long i = -1; i <= 1; ++i) {
            string p = to_string(prefix + i);
            string pp = p + string(p.rbegin() + (size & 1), p.rend());
            nums.insert(stol(pp));
        }

        long num = stol(n), minDiff = LONG_MAX, diff, minVal;
        nums.erase(num);

        for(long val: nums) {
            diff = abs(val - num);
            if(diff < minDiff) {
                minDiff = diff;
                minVal = val;
            } else if(diff == minDiff)
                minVal = min(minVal, val);
        }

        return to_string(minVal);
    }
};
```
