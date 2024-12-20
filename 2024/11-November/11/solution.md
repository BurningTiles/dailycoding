# Solution - 11 Nov 2024

---
## [2601. Prime Subtraction Operation](https://leetcode.com/problems/prime-subtraction-operation)

### cpp
```cpp
class Solution {
public:
    vector<int> getPrimes() {
        vector<int> primes = {2}, sieve(1001);
        for(int i=3; i<32; ++i) {
            if(!sieve[i]) {
                for(int j=i*i; j<=1000; j+=i)
                    sieve[j] = true;
            }
        }
        for(int i=3; i<=1000; i+=2)
            if(!sieve[i])
                primes.push_back(i);
        return primes;
    }

    bool primeSubOperation(vector<int>& nums) {
        vector<int> primes = getPrimes();

        for(int i=0; i<nums.size(); ++i) {
            auto ptr = lower_bound(primes.begin(), primes.end(), nums[i] - (i ? nums[i-1] : 0));
            if(ptr != primes.begin())
                nums[i] -= *prev(ptr);
            if(i && nums[i] <= nums[i-1])
                return false;
        }

        return true;
    }
};
```
