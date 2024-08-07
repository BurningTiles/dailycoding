# Solution - 27 Jul 2024

---
## [2976. Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i)

### cpp
```cpp
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<int>> charMap(26, vector<int>(26, INT_MAX));
        for(int i=0; i<26; ++i)
            charMap[i][i] = 0;
        
        for(int i=0; i<original.size(); ++i) {
            int from = original[i]-'a', to = changed[i]-'a';
            charMap[from][to] = min(charMap[from][to], cost[i]);
        }

        for(int mid=0; mid<26; ++mid) {
            for(int i=0; i<26; ++i) {
                if(charMap[i][mid] < INT_MAX) {
                    for(int j=0; j<26; ++j)
                        if(charMap[mid][j] < INT_MAX)
                            charMap[i][j] = min(charMap[i][j], charMap[i][mid] + charMap[mid][j]);
                }
            }
        }

        long long ans = 0;
        for(int i=0; i<source.size(); ++i) {
            if(charMap[source[i]-'a'][target[i]-'a'] == INT_MAX){
                cout << i << " " << source[i] << " " << target[i] << endl;
                return -1;
            }
            ans += charMap[source[i]-'a'][target[i]-'a'];
        }

        return ans;
    }
};
```
