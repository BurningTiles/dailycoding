# Solution - 01 Oct 2024

---
## [1497. Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k)

### cpp
```cpp
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        vector<int> cnt(k, 0);

        for(int i=0; i<arr.size(); ++i)
            cnt[(arr[i] % k + k) % k]++;

        if(cnt[0]&1) return false;

        for(int i=1; i<=k/2; ++i)
            if(cnt[i] != cnt[k-i]) return false;
        
        return true;
    }
};
```
