# Solution - 26 Oct 2023

---
## [823. Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors)

### cpp
```cpp
#define ll long long
const int MOD = 1e9+7;

class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        ios_base::sync_with_stdio(false),cin.tie(0);
        sort(arr.begin(), arr.end());
        unordered_map<ll, ll> um;
        ll ans = 0, lim, d;
        
        for(ll i=0; i<arr.size(); ++i) {
            um[arr[i]] = 1, lim = sqrt(arr[i]);
            for(int j=0; arr[j]<=lim; ++j) {
                d = arr[i]/arr[j];
                if(arr[i]%arr[j]==0 && um[d]) {
                    if(d==lim)
                        um[arr[i]] += um[d] * um[d];
                    else
                        um[arr[i]] += 2L * um[arr[j]] * um[d];
                    um[arr[i]] %= MOD;
                }
            }
            ans = (ans + um[arr[i]]) % MOD;
        }

        return ans;
    }
};
```
