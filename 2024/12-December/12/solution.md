# Solution - 12 Dec 2024

---
## [2558. Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile)

### cpp
```cpp
class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<long long> pq;

        for(int i=0; i<gifts.size(); ++i)
            pq.push(gifts[i]);

        while(k--) {
            long long tmp = pq.top(); pq.pop();
            pq.push(sqrt(tmp));
        }

        long long ans = 0;
        while(pq.size()) {
            ans += pq.top(); pq.pop();
        }

        return ans;
    }
};
```
