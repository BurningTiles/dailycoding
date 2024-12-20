# Solution - 20 Nov 2024

---
## [2516. Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right)

### cpp
```cpp
class Solution {
public:
    int takeCharacters(string s, int k) {
        if(k==0) return 0;
        int n = s.size(), ans = n, cnt[3] = {0};

        for(int i=0; i<n; ++i)
            cnt[s[i]-'a']++;

        if(cnt[0]<k || cnt[1]<k || cnt[2]<k)
            return -1;

        int i=n-1, j=n-1;

        while(i>=0) {
            cnt[s[i]-'a']--;
            
            while(cnt[0]<k || cnt[1]<k || cnt[2]<k) {
                cnt[s[j]-'a']++;
                --j;
            }

            --i;
            ans = min(ans, i+n-j);
        }
        
        return ans;
    }
};
```
