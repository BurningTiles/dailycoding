# Solution - 02 Nov 2024

---
## [2490. Circular Sentence](https://leetcode.com/problems/circular-sentence)

### cpp
```cpp
class Solution {
public:
    bool isCircularSentence(string sentence) {
        if(sentence.front() != sentence.back())
            return false;
        
        for(int i=1; i<sentence.size() - 1; ++i)
            if(sentence[i] == ' ' && sentence[i-1] != sentence[i+1])
                return false;
        
        return true;
    }
};
```
