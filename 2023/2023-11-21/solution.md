# Solution - 21 Nov 2023

---
## [1814. Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array)

### cpp
```cpp
class Solution {
public:
    long long rev(int n) {
        long long ans = 0;
        while(n) {
            ans = ans * 10 + n%10;
            n /= 10;
        }
        return ans;
    }

    int countNicePairs(vector<int>& nums) {
        unordered_map<long long, long long> um;
        for(auto &num:nums)
            um[num-rev(num)]++;
        
        long long ans=0;
        for(auto [sum, count]:um)
            if(count>1)
                ans += count*(count-1)/2;
        
        return ans %= 1000000007;
    }
};
```
