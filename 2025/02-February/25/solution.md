# Solution - 25 Feb 2025

---
## [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum)

### cpp
```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        long long ans = 0, sum = 0;

        for(int i=0; i<arr.size(); ++i) {
            sum += arr[i];
            ans += sum&1;
        }

        ans += (arr.size() - ans) * ans;
        return ans % 1000000007;
    }
};
```
