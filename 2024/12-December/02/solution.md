# Solution - 02 Dec 2024

---
## [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence)

### cpp
```cpp
class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        int wordCnt = 0, start = 1;

        for(int i=0; i<sentence.size(); ++i) {
            if(start) ++wordCnt;

            if(sentence[i] == ' ')
                start = 1;
            else {
                if(start) {
                    int j=0;
                    while(j<searchWord.size() && searchWord[j]==sentence[i+j])
                        ++j;
                    if(j == searchWord.size())
                        return wordCnt;
                }
                start = 0;
            }
        }

        return -1;
    }
};
```
