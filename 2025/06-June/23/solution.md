# Solution - 23 Jun 2025

---
## [2081. Sum of k-Mirror Numbers](https://leetcode.com/problems/sum-of-k-mirror-numbers)

### cpp
```cpp
class Solution {
    vector<long long> mirror1{0}, mirror2{0};
public:
    long long isMirror(long long num, int base) {
        long long mul = 1;
        while (mul * base <= num)
            mul *= base;

        for(; num; mul /= base * base) {
            if(num / mul != num % base)
                return false;
            num = (num - (num / mul) * mul - num % base) / base;
        }

        return true;
    }

    long long generate(int dig, int n, int k, long long first_mul) {
        vector<long long> mirror;
        long long ans = 0;

        for(int i=0; n>0 && i<10; ++i) {
            for(int j=0; n>0 && j<mirror1.size(); ++j) {
                mirror.push_back(first_mul * i + mirror1[j] * 10 + i);

                if(i != 0 && isMirror(mirror.back(), k)) {
                    ans += mirror.back();
                    --n;
                }
            }
        }

        swap(mirror1, mirror2);
        swap(mirror2, mirror);

        return ans + (n == 0 ? 0 : generate(dig + 1, n, k, first_mul * 10));
    }

    long long kMirror(int k, int n) {
        long long ans = 0;

        for(int i=1; n>0 && i<10; ++i) {
            mirror2.push_back(i);
            if(isMirror(i, k)) {
                ans += i;
                --n;
            }
        }

        return ans + generate(2, n, k, 10);
    }
};
```
