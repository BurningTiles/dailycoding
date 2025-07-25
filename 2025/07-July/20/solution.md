# Solution - 20 Jul 2025

---
## [1948. Delete Duplicate Folders in System](https://leetcode.com/problems/delete-duplicate-folders-in-system)

### cpp
```cpp
class Trie {
public:
    unordered_map<string, Trie*> links;
    string id = "";
    bool mark = 0;
    Trie(string id = ""): id(id) {}

    void insert(vector<string> &path) {
        Trie *Node = this;
        for (string &s:path) {
            if(!Node->links.count(s))
                Node->links[s] = new Trie(s);
            Node = Node->links[s];
        }
    }
};

class Solution {
public:
    Trie trie;
    unordered_map<string, Trie*> mp;
    vector<vector<string>> ans;

    string serial(Trie *node) {
        if(node->links.empty())
            return "";
        
        vector<pair<string, Trie*>> sorted(node->links.begin(), node->links.end());

        sort(sorted.begin(), sorted.end());

        string dir;
        for(auto &[id, child]:sorted)
            dir += "(" + id + serial(child) + ")";
        
        if(mp.count(dir)) {
            mp[dir]->mark = 1;
            node->mark = 1;
        }
        else
            mp[dir] = node;
        
        return dir;
    }

    void to_ans(Trie *node, vector<string> &path) {
        for(auto &[id, child]: node->links) {
            if(child->mark)
                continue;
            path.push_back(id);
            ans.push_back(path);
            to_ans(child, path);
            path.pop_back();
        }
    }

    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        for(auto &path: paths)
            trie.insert(path);
        
        serial(&trie);
        vector<string> path;
        to_ans(&trie, path);
        return ans;
    }
};
```
