# Solution - 10 Apr 2024

---
## [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order)

### cpp
```cpp
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.rbegin(), deck.rend());
        deque<int> q; q.push_front(deck[0]);

        for(int i=1; i<deck.size(); ++i) {
            q.push_front(q.back()); 
            q.pop_back();
            q.push_front(deck[i]);
        }

        vector<int> ans(q.begin(), q.end());
        return ans;
    }
};
```
