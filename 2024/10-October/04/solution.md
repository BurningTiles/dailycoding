# Solution - 04 Oct 2024

---
## [2491. Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill)

### cpp
```cpp
class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        unordered_map<int, int> umap;
        long long totalSum = 0, ans = 0, teamSkill=0;

        for(int s:skill) {
            umap[s]++;
            totalSum += s;
        }

        teamSkill = totalSum / (skill.size()/2);

        for(int s:skill) {
            if(!umap[s]) continue;
            umap[s]--;

            long long partner = teamSkill - s;
            
            if(!umap[partner])
                return -1;
            umap[partner]--;

            ans += s * partner;
        }

        return ans;
    }
};
```
