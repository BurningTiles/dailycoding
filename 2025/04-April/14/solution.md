# Solution - 14 Apr 2025

---
## [1534. Count Good Triplets](https://leetcode.com/problems/count-good-triplets)

### cpp
```cpp
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int ans = 0;

        for (int i = 0; i < arr.size(); ++i) {
            for (int j = i + 1; j < arr.size(); ++j) {
                if (abs(arr[i] - arr[j]) <= a)
                    for (int k = j + 1; k < arr.size(); ++k) {
                        if (abs(arr[j] - arr[k]) <= b &&
                            abs(arr[i] - arr[k]) <= c)
                            ++ans;
                    }
            }
        }

        return ans;
    }
};
```
