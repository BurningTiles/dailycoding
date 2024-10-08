# Solution - 06 Oct 2024

---
## [1813. Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii)

### cpp
```cpp
class Solution {
public:
    deque<string> strToVec(string s) {
        stringstream ss(s);
        deque<string> ans;
        string tmp;
        
        while(ss >> tmp)
            ans.push_back(tmp);

        return ans;
    }

    bool areSentencesSimilar(string sentence1, string sentence2) {
        deque<string> v1 = strToVec(sentence1), v2 = strToVec(sentence2);
        
        while(v1.size() && v2.size() && v1.front() == v2.front())
            v1.pop_front(), v2.pop_front();
        
        while(v1.size() && v2.size() && v1.back() == v2.back())
            v1.pop_back(), v2.pop_back();
        
        return v1.empty() || v2.empty();
    }
};
```
