# Solution - 07 Jun 2025

---
## [3170. Lexicographically Minimum String After Removing Stars](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars)

### cpp
```cpp
class Solution {
public:
    string clearStars(string s) {
        priority_queue<pair<char, int>, vector<pair<char, int>>, greater<pair<char, int>>> pq;

        for(int i=0; i<s.size(); ++i) {
            if(s[i] == '*') {
                if(pq.size()) {
                    s[-pq.top().second] = '*';
                    pq.pop();
                }
            } else {
                pq.push({s[i], -i});
            }
        }

        string ans;
        for(char c:s) if(c >= 'a') ans.push_back(c);
        return ans;
    }
};
```
