# Solution - 07 Dec 2024

---
## [1760. Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag)

### cpp
```cpp
class Solution {
public:
    int minimumSize(vector<int>& A, int k) {
        int left = 1, right = 1e9;
        while (left < right) {
            int mid = (left + right) / 2, count = 0;
            for (int a : A)
                count += (a - 1) / mid;
            if (count > k)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
};
```
