# Solution - 10 Apr 2025

---
## [2999. Count the Number of Powerful Integers](https://leetcode.com/problems/count-the-number-of-powerful-integers)

### cpp
```cpp
class Solution {
public:
    long long getPowerfulInt(const string num, const int limit, const string s) {
        if(num.size() < s.size())
            return 0;
        if(num.size() == s.size())
            return num >= s ? 1 : 0;

        string _s = num.substr(num.size() - s.size());

        long long ans = 0;
        int n = num.size() - s.size();

        for(int i=0; i<n; ++i) {
            if(limit < num[i]-'0') {
                ans += (long long) pow(limit + 1, n-i);
                return ans;
            }

            ans += (long long) (num[i] - '0') * pow(limit + 1, n - 1 - i);
        }
        
        if(_s >= s)
            ++ans;
        return ans;
    }

    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        return getPowerfulInt(to_string(finish), limit, s) - getPowerfulInt(to_string(start-1), limit, s);
    }
};
```
