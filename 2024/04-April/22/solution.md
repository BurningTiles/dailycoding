# Solution - 22 Apr 2024

---
## [752. Open the Lock](https://leetcode.com/problems/open-the-lock)

### cpp
```cpp
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        unordered_set<string> used;

        if(dead.count("0000")) return -1;

        queue<string> q;
        q.push("0000");

        int moves = 0;

        while(q.size()) {
            int size = q.size();
            for(int t=0; t<size; ++t) {
                string s = q.front(); q.pop();
                
                if(s == target)
                    return moves;
                
                for(int i=0; i<4; ++i)
                    for(int diff: {-1, 1}) {
                        int digit = (s[i]-'0' + diff + 10) % 10;
                        string tmp = s;
                        tmp[i] = '0' + digit;

                        if(!used.count(tmp) && !dead.count(tmp))
                            used.insert(tmp), q.push(tmp);
                    }
            }
            ++moves;
        }

        return -1;
    }
};
```
