# Solution - 07 Jun 2024

---
## [648. Replace Words](https://leetcode.com/problems/replace-words)

### cpp
```cpp
class Trie {
public:
    bool end;
    Trie *next[26];

    Trie() {
        end = false;
        for(int i=0; i<26; ++i) next[i] = NULL;
    }
};

class Solution {
    Trie *root = new Trie();

public:
    void insert(string word) {
        Trie *curr = root;

        for(char ch: word) {
            int i = ch - 'a';
            if(!curr->next[i])
                curr->next[i] = new Trie();
            curr = curr->next[i];
        }

        curr->end = true;
    }

    int search(string word) {
        Trie *curr = root;
        int len = 0;

        for(int ch: word) {
            ++len;
            int i = ch - 'a';

            if(!curr->next[i])
                return INT_MAX;
            
            curr = curr->next[i];

            if(curr->end) return len;
        }
        return INT_MAX;
    }

    string replaceWords(vector<string>& dictionary, string sentence) {
        for(auto word: dictionary) 
            insert(word);

        string ans = "", tmp = "";

        for(char i: sentence) {
            if(i==' ') {
                ans += tmp.substr(0, search(tmp));
                ans += " ";
                tmp = "";
            } 
            else 
                tmp += i;
        }

        ans += tmp.substr(0, search(tmp));
        return ans;
    }
};
```
