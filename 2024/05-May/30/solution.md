# Solution - 30 May 2024

---
## [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor)

### cpp
```cpp
class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int n = arr.size(), ans = 0, prefix = 0;
        unordered_map<int, int> count = {{0,1}}, total;

        for(int i=0; i<n; ++i) {
            prefix ^= arr[i];
            ans += count[prefix]++ * i - total[prefix];
            total[prefix] += i + 1;
        }

        return ans;
    }
};
```
